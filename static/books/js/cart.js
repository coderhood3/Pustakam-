// Cart interactions
document.addEventListener('DOMContentLoaded', () => {
    // Future: AJAX add to cart without reload
    const addToCartForms = document.querySelectorAll('form[action*="add_to_cart"]');
    addToCartForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            // Optional: Add flying animation to cart icon
        });
    });
});
