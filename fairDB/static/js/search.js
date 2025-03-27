document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('#search-bar input');
    const suggestionsList = document.querySelector('#suggestions-list');

    suggestionsList.style.display = 'none'; // Hide suggestions initially

    searchInput.addEventListener('input', function() {
        const query = searchInput.value;
        if (query.length > 0) {
            fetch(`/api/search/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsList.innerHTML = '';
                    if (data.results.length > 0) {
                        suggestionsList.style.display = 'block'; // Show suggestions
                        data.results.forEach(item => {
                            const li = document.createElement('li');
                            const a = document.createElement('a');
                            a.href = `/product/${item.barcode}/`;
                            a.textContent = item.name;
                            li.appendChild(a);
                            suggestionsList.appendChild(li);
                        });
                    } else {
                        suggestionsList.style.display = 'none'; // Hide suggestions if no results
                    }
                });
        } else {
            suggestionsList.style.display = 'none'; // Hide suggestions if input is empty
        }
    });

    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            const query = searchInput.value;
            window.location.href = `/product/${query}/`;
        }
    });
});