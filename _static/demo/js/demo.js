
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const categoryFilter = document.getElementById('category-filter');
    const resultsCount = document.getElementById('results-count');
    const experimentGrid = document.querySelector('.experiment-grid');

    if (!searchInput || !categoryFilter || !resultsCount || !experimentGrid) {
        return;
    }

    const cards = Array.from(
        experimentGrid.querySelectorAll('.experiment-grid, .col')
    ).filter(function (card) {
        return card.querySelector('.card');
    });

    const categoryMap = {
        'Decision-Making': 'decision-making',
        'Real Effort Task': 'real-effort-task',
        'Shopping Simulation': 'shopping-simulation',
        'Puzzle & Problem Solving': 'puzzle-problem-solving',
        'Research Experiment': 'research-experiment'
    };

    const noResults = document.querySelector('.no-results');
    noResults.hidden = true;

    function filterExperiments() {
        const keyword = searchInput.value.trim().toLowerCase();
        const selectedCategory = categoryFilter.value;
        let visibleCount = 0;

        cards.forEach(function (card) {
            const searchableText = card.textContent.toLowerCase();
            const categoryElement = card.querySelector('.badge');
            const categoryName = categoryElement
                ? categoryElement.textContent.trim()
                : 'Research Experiment';

            const cardCategory = categoryMap[categoryName] || 'research-experiment';
            const matchesKeyword = searchableText.includes(keyword);
            const matchesCategory =
                selectedCategory === 'all' ||
                cardCategory === selectedCategory;

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