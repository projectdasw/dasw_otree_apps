let myCart = document.getElementById('cart-body');
let cartSubtotal = document.getElementById('cart-subtotal');
let cartTax = document.getElementById('cart-tax');
let cartDiscount = document.getElementById('cart-discount');
let cartTotal = document.getElementById('cart-total');

function addToCart(ele) {
    modifyCart(ele.value, 1);
}

function removeFromCart(ele) {
    modifyCart(ele.value, -1);
}

function updateProductQuantities(items) {
    // Reset semua quantity menjadi 0
    document.querySelectorAll('[id^="quantity-"]').forEach(function (element) {
        element.innerText = '0';
    });

    // Nonaktifkan semua tombol minus
    document.querySelectorAll('[id^="remove-"]').forEach(function (button) {
        button.disabled = true;
    });

    // Update quantity produk yang ada di cart
    for (let item of items) {
        let quantityElement = document.getElementById(`quantity-${item.sku}`);
        let removeButton = document.getElementById(`remove-${item.sku}`);
        if (quantityElement) {
            quantityElement.innerText = item.quantity;
        }

        // Aktifkan tombol minus jika quantity > 0
        if (removeButton && item.quantity > 0) {
            removeButton.disabled = false;
        }
    }
}

function modifyCart(sku, delta) {
    liveSend({'sku': sku, 'delta': delta});
}

function cu(amount) {
    return `${amount} points`;
}

function liveRecv(data) {
    let html = '';

    for (let item of data.items) {
        html += `
            <tr>
                <td>${item.name}</td>
                <td>${item.quantity}</td>
                <td>${cu(item.total_price)}</td>
            </tr>
        `;
    }

    myCart.innerHTML = html;

    // Update quantity pada katalog
    updateProductQuantities(data.items);

    // Update cart summary
    cartSubtotal.innerText = cu(data.subtotal);
    cartTax.innerText = cu(data.tax);
    cartDiscount.innerText = cu(data.discount);
    cartTotal.innerText = cu(data.total_price);
}

document.addEventListener("DOMContentLoaded", function (event) {
    liveSend({});
});