document.addEventListener('DOMContentLoaded', () => {
    console.log('Cart page loaded');

    // Add remove item animation
    const removeButtons = document.querySelectorAll('.btn-remove');
    removeButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const item = btn.closest('.cart-item');
            if (item) {
                item.style.opacity = '0.5';
                item.style.pointerEvents = 'none';
            }
        });
    });
});
