document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', function() {
            navLinks.classList.toggle('active');
        });

        document.addEventListener('click', function(e) {
            if (!mobileMenuBtn.contains(e.target) && !navLinks.contains(e.target)) {
                navLinks.classList.remove('active');
            }
        });
    }

    const inputAge = document.getElementById('input-age');
    const inputDob = document.getElementById('input-dob');
    const ageInput = document.getElementById('age-input');
    const dobInput = document.getElementById('dob-input');

    if (inputAge && inputDob) {
        inputAge.addEventListener('change', function() {
            ageInput.classList.remove('hidden');
            dobInput.classList.add('hidden');
            document.getElementById('age').required = true;
            document.getElementById('dob').required = false;
        });

        inputDob.addEventListener('change', function() {
            ageInput.classList.add('hidden');
            dobInput.classList.remove('hidden');
            document.getElementById('age').required = false;
            document.getElementById('dob').required = true;
        });
    }

    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[type="number"], input[type="text"], input[type="date"]');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });
            input.addEventListener('blur', function() {
                this.parentElement.classList.remove('focused');
            });
        });
    });

    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.tool-card, .feature, .stat-card, .info-card');
        elements.forEach(element => {
            const rect = element.getBoundingClientRect();
            const isVisible = rect.top < window.innerHeight - 100;
            if (isVisible) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };

    const toolCards = document.querySelectorAll('.tool-card, .feature, .stat-card, .info-card');
    toolCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });

    animateOnScroll();
    window.addEventListener('scroll', animateOnScroll);
});
