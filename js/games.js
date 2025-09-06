// Get the search bar (first input with class 'search-bar' in this context)
const searchBar = document.querySelector('.search-bar');
searchBar.addEventListener('input', function (e) {
    const query = e.target.value.toLowerCase();
    // Select all game cards (each .games-section-menu > div)
    const allCards = document.querySelectorAll('.games-section-menu > div');
    allCards.forEach(card => {
        // Check the text content of the card (including title and description)
        const text = card.textContent.toLowerCase();
        if (text.includes(query)) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
});