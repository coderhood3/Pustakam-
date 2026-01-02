// Star Rating Interaction
document.addEventListener('DOMContentLoaded', () => {
    const starContainer = document.querySelector('#star-rating-input');
    if (starContainer) {
        const stars = starContainer.querySelectorAll('i');
        const hiddenInput = document.querySelector('#id_rating');

        stars.forEach(star => {
            star.addEventListener('click', () => {
                const value = star.dataset.value;
                hiddenInput.value = value;
                updateStars(value);
            });

            star.addEventListener('mouseover', () => {
                updateStars(star.dataset.value);
            });
        });

        starContainer.addEventListener('mouseleave', () => {
            updateStars(hiddenInput.value || 0);
        });

        function updateStars(value) {
            stars.forEach(s => {
                if (s.dataset.value <= value) {
                    s.classList.remove('fa-regular');
                    s.classList.add('fa-solid');
                    s.style.color = 'var(--accent-500)';
                } else {
                    s.classList.remove('fa-solid');
                    s.classList.add('fa-regular');
                    s.style.color = '#cbd5e1';
                }
            });
        }
    }
});
