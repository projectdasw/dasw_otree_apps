from otree.api import *
import json

doc = """
Shopping app
"""


class Product(ExtraModel):
    sku = models.StringField()
    name = models.StringField()
    image_png = models.StringField()
    unit_price = models.CurrencyField()


def load_products():
    rows = read_csv(__name__ + '/catalog.csv', Product)
    for row in rows:
        row['image_path'] = 'grocery/{}.png'.format(row['image_png'])
    return rows


class C(BaseConstants):
    NAME_IN_URL = 'shop_apps'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TAX_RATE = 0.10
    DISCOUNT_RATE = 0.30
    PRODUCTS = load_products()
    # SKU = 'stock keeping unit' = product ID
    PRODUCTS_DICT = {row['sku']: row for row in PRODUCTS}


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    subtotal = models.CurrencyField(initial=0)
    tax = models.CurrencyField(initial=0)
    discount = models.CurrencyField(initial=0)
    total_price = models.CurrencyField(initial=0)
    purchased = models.LongStringField()


class Item(ExtraModel):
    player = models.Link(Player)
    sku = models.StringField()
    name = models.StringField()
    quantity = models.IntegerField()
    unit_price = models.CurrencyField()


def calculate_cart(player):
    items = Item.filter(player=player)

    subtotal = sum(
        total_price(item)
        for item in items
    )

    tax = subtotal * C.TAX_RATE
    discount = subtotal * C.DISCOUNT_RATE
    cart_total = subtotal + tax - discount

    return subtotal, tax, discount, cart_total

def total_price(item: Item):
    return item.quantity * item.unit_price

def to_dict(item: Item):
    return dict(
        sku=item.sku,
        name=item.name,
        quantity=item.quantity,
        unit_price=item.unit_price,
        total_price=total_price(item),
    )


def live_method(player: Player, data):
    if 'sku' in data:
        sku = data['sku']
        delta = data['delta']
        product = C.PRODUCTS_DICT[sku]

        matches = Item.filter(player=player, sku=sku)

        if matches:
            [item] = matches
            item.quantity += delta

            if item.quantity <= 0:
                item.delete()

        else:
            if delta > 0:
                Item.create(
                    player=player,
                    quantity=delta,
                    sku=sku,
                    name=product['name'],
                    unit_price=product['unit_price'],
                )

    items = Item.filter(player=player)

    subtotal, tax, discount, cart_total = calculate_cart(player)

    player.total_price = cart_total

    item_dicts = [to_dict(item) for item in items]

    return {
        player.id_in_group: dict(
            items=item_dicts,
            subtotal=subtotal,
            tax=tax,
            discount=discount,
            total_price=cart_total,
        )
    }


# PAGES
class game(Page):
    live_method = live_method

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        items = Item.filter(player=player)

        subtotal, tax, discount, cart_total = calculate_cart(player)

        player.subtotal = subtotal
        player.tax = tax
        player.discount = discount
        player.total_price = cart_total

        purchased_items = [
            {
                'name': item.name,
                'quantity': item.quantity,
                'unit_price': str(item.unit_price),
            }
            for item in items
        ]

        player.purchased = json.dumps(purchased_items, ensure_ascii=False)


class results(Page):
    @staticmethod
    def vars_for_template(player: Player):

        items = Item.filter(player=player)

        return dict(
            items=[
                to_dict(item)
                for item in items
            ]
        )


page_sequence = [game, results]
