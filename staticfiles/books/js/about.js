document.addEventListener('DOMContentLoaded', () => {
    console.log('About page loaded');

    // Add simple fade-in effect to sections
    const sections = document.querySelectorAll('.about-section');
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = `all 0.6s ease ${index * 0.2}s`;

        setTimeout(() => {
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, 100);
    });
});
