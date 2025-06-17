document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('email-form');
    if (form) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('Email').value;
            const phone = document.getElementById('Phone').value;
            const address = document.getElementById('Address').value;
            const message = document.getElementById('Message').value;

            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    email: email,
                    phone: phone,
                    address: address,
                    message: message
                })
            });

            if (response.ok) {
                form.reset();
                document.querySelector('.success-message').style.display = 'block';
                document.querySelector('.error-message').style.display = 'none';
            } else {
                document.querySelector('.success-message').style.display = 'none';
                document.querySelector('.error-message').style.display = 'block';
            }
        });
    }
});
