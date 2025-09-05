fetch('/data/blogs/blogs-pages.json')
    .then(res => res.json())
    .then(blogPages => {
        const searchBar = document.getElementById('searchBar');
        const resultContainer = document.createElement('div');
        resultContainer.id = 'searchResults';
        resultContainer.style.position = 'absolute';
        resultContainer.style.background = '#fff';
        resultContainer.style.border = '1px solid #ccc';
        resultContainer.style.width = searchBar.offsetWidth + 'px';
        resultContainer.style.zIndex = '1000';
        resultContainer.style.display = 'none';
        searchBar.parentNode.appendChild(resultContainer);

        searchBar.addEventListener('input', function (e) {
            const query = e.target.value.toLowerCase();
            resultContainer.innerHTML = '';
            if (query.length < 2) {
                resultContainer.style.display = 'none';
                return;
            }
            const matches = blogPages.filter(page => page.title.toLowerCase().includes(query));
            if (matches.length > 0) {
                matches.forEach(page => {
                    const link = document.createElement('a');
                    link.href = page.url;
                    link.textContent = page.title;
                    link.style.display = 'block';
                    link.style.padding = '0.5em 1em';
                    link.style.color = '#0077cc';
                    link.style.textDecoration = 'none';
                    link.style.borderBottom = '1px solid #eee';
                    link.addEventListener('mouseover', () => link.style.background = '#f0f8ff');
                    link.addEventListener('mouseout', () => link.style.background = 'transparent');
                    resultContainer.appendChild(link);
                });
                resultContainer.style.display = 'block';
            } else {
                const noResult = document.createElement('div');
                noResult.textContent = 'No results found';
                noResult.style.padding = '0.5em 1em';
                resultContainer.appendChild(noResult);
                resultContainer.style.display = 'block';
            }
        });

        // Hide results when clicking outside
        document.addEventListener('click', function (e) {
            if (!searchBar.contains(e.target) && !resultContainer.contains(e.target)) {
                resultContainer.style.display = 'none';
            }
        });
    });