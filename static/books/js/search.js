// Search functionality
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('input[name="q"]');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            // Future: Implement AJAX auto-suggest here
            console.log('Searching for:', e.target.value);
        });
    }
});
