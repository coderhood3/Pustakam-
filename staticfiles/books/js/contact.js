document.addEventListener('DOMContentLoaded', () => {
    console.log('Contact page loaded');

    // Simple form submission animation/mock
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (e) => {
            // Let the backend handle it, but we can fancy it up later
            const btn = form.querySelector('button[type="submit"]');
            if (btn) {
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
                btn.style.opacity = '0.8';
            }
        });
    }
});
