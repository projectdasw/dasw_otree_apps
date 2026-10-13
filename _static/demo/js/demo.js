
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('dasw-search-input');
    const categoryFilter = document.getElementById('dasw-category-filter');
    const resultsCount = document.getElementById('dasw-results-count');
    const experimentGrid = document.querySelector('.dasw-experiment-grid');

    if (!searchInput || !categoryFilter || !resultsCount || !experimentGrid) {
        return;
    }

    const cards = Array.from(
        experimentGrid.querySelectorAll('.dasw-experiment-card')
    );

    const categoryMap = {
        'Decision-Making': 'decision-making',
        'Real Effort Task': 'real-effort-task',
        'Shopping Simulation': 'shopping-simulation',
        'Puzzle & Problem Solving': 'puzzle-problem-solving',
        'Research Experiment': 'research-experiment'
    };

    const noResults = document.createElement('div');
    noResults.className = 'dasw-no-results';
    noResults.hidden = true;
    noResults.innerHTML = `
        <h3>No experiments found</h3>
        <p>Try another keyword or select a different category.</p>
    `;

    experimentGrid.appendChild(noResults);

    function filterExperiments() {
        const keyword = searchInput.value.trim().toLowerCase();
        const selectedCategory = categoryFilter.value;
        let visibleCount = 0;

        cards.forEach(function (card) {
            const searchableText = card.textContent.toLowerCase();

            const categoryElement = card.querySelector('.dasw-category');
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

        resultsCount.textContent =
            'Showing ' + visibleCount + ' of ' + cards.length + ' experiments';
    }

    searchInput.addEventListener('input', filterExperiments);
    categoryFilter.addEventListener('change', filterExperiments);

    filterExperiments();
});
