document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('star-rating-form');
    const ratingInputs = form.querySelectorAll('input[name="rating"]');
    const feedbackDiv = document.getElementById('rating-feedback');

    const url = window.location.pathname;
    const urlParts = url.split('/');
    const barcode = urlParts[urlParts.length - 2];

    ratingInputs.forEach(input => {
        input.addEventListener('change', function() {
            const rating = parseInt(this.value);
            const csrftoken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

            fetch('/rate-product/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    rating: rating,
                    barcode: barcode
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    feedbackDiv.innerHTML = '<span style="color: green;">Vielen Dank für deine Bewertung!</span>';

                    updateCommunityRating(data.new_gold_stars, data.new_gray_stars);

                    ratingInputs.forEach(input => input.disabled = true);
                } else {
                    throw new Error(data.error || 'Ein unbekannter Fehler ist aufgetreten.');
                }
            })
            .catch(error => {
                feedbackDiv.innerHTML = `<span style="color: red;">Fehler: ${error.message}</span>`;
            });
        });
    });

    function updateCommunityRating(goldStars, grayStars) {
        const ratingDiv = document.querySelector('.community-rating div');
        let starsHTML = '';

        for (let i = 0; i < goldStars; i++) {
            starsHTML += '<span class="star-gold">★ </span>';
        }

        for (let i = 0; i < grayStars; i++) {
            starsHTML += '<span class="star-gray">★ </span>';
        }

        ratingDiv.innerHTML = starsHTML;
    }
});