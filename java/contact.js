document.addEventListener('DOMContentLoaded', function() {
    console.log('Contact form script loaded');
    const form = document.getElementById('email-form');
    const successMessage = document.querySelector('.w-form-done');
    const errorMessage = document.querySelector('.w-form-fail');

    if (form) {
        console.log('Found contact form');
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            console.log('Form submission started');
            
            try {
                const formData = {
                    name: document.getElementById('name').value,
                    email: document.getElementById('Email').value,
                    phone: document.getElementById('Phone').value,
                    address: document.getElementById('Address').value,
                    message: document.getElementById('Message').value
                };
                console.log('Form data:', formData);

                console.log('Sending request to backend...');
                const response = await fetch('http://localhost:5000/api/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });
                console.log('Response received:', response.status);

                if (response.ok) {
                    console.log('Success:', successData);
                    form.reset();
                    successMessage.style.display = 'block';
                    errorMessage.style.display = 'none';
                } else {
                    console.error('Server error:', errorData);
                    errorMessage.style.display = 'block';
                    successMessage.style.display = 'none';
                }
            } catch (error) {
                console.error('Network error:', error);
                errorMessage.style.display = 'block';
                successMessage.style.display = 'none';
            }
        });
    } else {
        console.error('Contact form not found in the document');
    }
});
