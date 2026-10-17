
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const categoryFilter = document.getElementById('category-filter');
    const resultsCount = document.getElementById('results-count');
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
            const matchesCategory = selectedCategory === 'all' || category === selectedCategory
                || status === selectedCategory;

            const isVisible = matchesKeyword && matchesCategory;

            card.hidden = !isVisible;

            if (isVisible) {
                visibleCount++;
            }
        });

        noResults.hidden = visibleCount > 0;
        resultsCount.textContent = 'Showing ' + visibleCount + ' of ' + cards.length + ' experiments';
    }

    searchInput.addEventListener('input', filterExperiments);
    categoryFilter.addEventListener('change', filterExperiments);

    filterExperiments();
});