document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.footer-from');
    forms.forEach(function(form) {
        const input = form.querySelector('input[type="email"]');
        const successMessage = form.parentElement.querySelector('.w-form-done');
        const errorMessage = form.parentElement.querySelector('.w-form-fail');
        if (form && input) {
            form.addEventListener('submit', async function(e) {
                e.preventDefault();
                const email = input.value.trim();
                if (!email) {
                    errorMessage.style.display = 'block';
                    errorMessage.textContent = 'Please enter a valid email.';
                    successMessage.style.display = 'none';
                    return;
                }
                try {
                    const response = await fetch('http://localhost:5000/api/newsletter/subscribe', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({ email })
                    });
                    const data = await response.json();
                    if (response.ok) {
                        form.reset();
                        successMessage.style.display = 'block';
                        errorMessage.style.display = 'none';
                        successMessage.textContent = data.message || 'Subscribed successfully!';
                    } else {
                        errorMessage.style.display = 'block';
                        successMessage.style.display = 'none';
                        errorMessage.textContent = data.error || data.message || 'Subscription failed.';
                    }
                } catch (err) {
                    errorMessage.style.display = 'block';
                    successMessage.style.display = 'none';
                    errorMessage.textContent = 'Network error. Please try again.';
                }
            });
        }
    });
});
