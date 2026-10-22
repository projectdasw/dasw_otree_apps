
document.addEventListener('DOMContentLoaded', function () {
    let activeCategory = 'all';
    const searchInput = document.getElementById('search-input');
    const categoryFilter = document.getElementById('category-filter');
    const categoryBadges = document.querySelectorAll('.category-filter-badge');
    const activeFilterSummary = document.getElementById('active-filter-summary');
    const resultsCount = document.getElementById('results-count');
    const resetButton = document.getElementById('reset-filter');
    const experimentGrid = document.querySelector('.experiment-grid');

    if (!searchInput || !categoryFilter || !resultsCount || !experimentGrid) {
        return;
    }

    const cards = Array.from(experimentGrid.querySelectorAll('.experiment-grid, .col')
        ).filter(function (card) {
            return card.querySelector('.card');
        });

    const noResults = document.querySelector('.no-results');
    noResults.hidden = true;

    function updateCategoryCounts() {
        const counts = {all: cards.length};
        cards.forEach(function (card) {
            const category = (card.querySelector('[data-category]')?.dataset.category
                || 'research-experiment').trim().replace(/\s+/g, '');

            counts[category] = (counts[category] || 0) + 1;
        });

        document.querySelectorAll('[data-category-count]').forEach(function (badge) {
            const category = badge.dataset.categoryCount;
            badge.textContent = '(' + (counts[category] || 0) + ')';
        });
    }

    function filterExperiments() {
        const keyword = searchInput.value.trim().toLowerCase();
        const selectedCategory = categoryFilter.value;
        let visibleCount = 0;

        cards.forEach(function (card) {
            const searchableText = card.textContent.toLowerCase();
            const category = (card.querySelector('[data-category]')?.dataset.category
                || 'research-experiment').trim().replace(/\s+/g, '');
            const statusElement = card.querySelector('[data-status]');
            const status = statusElement ? statusElement.dataset.status.trim() : '';
            const matchesKeyword = searchableText.includes(keyword);
            const matchesStatus = selectedCategory === 'all' || category === selectedCategory
                || status === selectedCategory;
            const matchesAppCategory = activeCategory === 'all' || category === activeCategory;
            const isVisible = matchesKeyword && matchesStatus && matchesAppCategory;

            card.hidden = !isVisible;

            if (isVisible) {
                visibleCount++;
            }
        });

        noResults.hidden = visibleCount > 0;
        resultsCount.textContent = 'Showing ' + visibleCount + ' of ' + cards.length + ' experiments';
    }

    function updateActiveFilters() {
        const selectedStatus = categoryFilter.value;
        const selectedCategory = activeCategory;
        const keyword = searchInput.value.trim();
        const hasStatusFilter = selectedStatus !== 'all';
        const hasCategoryFilter = selectedCategory !== 'all';
        const hasKeyword = keyword !== '';
        const hasActiveFilter = hasStatusFilter || hasCategoryFilter || hasKeyword;

        // Tombol reset hanya muncul jika ada filter aktif
        resetButton.hidden = !hasActiveFilter;

        // Sembunyikan ringkasan jika tidak ada filter aktif
        activeFilterSummary.hidden = !hasActiveFilter;
        activeFilterSummary.replaceChildren();

        if (!hasActiveFilter) {
            return;
        }

        const heading = document.createElement('span');
        heading.className = 'text-muted small';
        heading.textContent = 'Active filters:';
        activeFilterSummary.appendChild(heading);

        function addFilterLabel(label) {
            const badge = document.createElement('span');
            badge.className = 'badge text-bg-light border text-dark';
            badge.textContent = label;
            activeFilterSummary.appendChild(badge);
        }

        if (hasCategoryFilter) {
        const badge = document.querySelector(
            `[data-category-filter="${selectedCategory}"]`
        );

        addFilterLabel('Category: ' + (badge?.textContent.trim().replace(/\(\d+\)/, '').trim()
                || selectedCategory));
    }

    if (hasStatusFilter) {
        const selectedOption =
            categoryFilter.selectedOptions[0];

        addFilterLabel(
            'Status: ' + selectedOption.textContent.trim()
        );
    }

    if (hasKeyword) {
        addFilterLabel('Search: ' + keyword);
    }
}

    categoryBadges.forEach(function (badge) {
        badge.addEventListener('click', function () {
            activeCategory = badge.dataset.categoryFilter;
            categoryBadges.forEach(function (item) {
                const isActive = item === badge;
                item.classList.toggle('active', isActive);
                item.setAttribute('aria-pressed', String(isActive));
            });

            filterExperiments();
            updateActiveFilters();
        });
    });

    searchInput.addEventListener('input', function () {
        filterExperiments();
        updateActiveFilters();
    });

    categoryFilter.addEventListener('change', function () {
        filterExperiments();
        updateActiveFilters();
    });

    if (resetButton) {
        resetButton.addEventListener('click', function () {
            searchInput.value = '';
            categoryFilter.value = 'all';
            activeCategory = 'all';

            categoryBadges.forEach(function (badge) {
                const isActive = badge.dataset.categoryFilter === 'all';
                badge.classList.toggle('active', isActive);
                badge.setAttribute('aria-pressed', String(isActive));
            });

            filterExperiments();
            updateActiveFilters();
            searchInput.focus();
        });
    }

    updateCategoryCounts();
    filterExperiments();
    updateActiveFilters();
});