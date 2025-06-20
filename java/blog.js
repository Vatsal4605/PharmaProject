document.addEventListener('DOMContentLoaded', () => {
    const blogImages = [
        'blog_images/blog1.jpeg',
        'blog_images/blog2.jpeg',
        'blog_images/blog3.jpeg',
        'blog_images/blog4.jpeg',
        'blog_images/blog5.jpeg',
        'blog_images/blog6.jpeg',
        'blog_images/blog7.jpeg',
        'blog_images/blog8.jpeg',
        'blog_images/blog9.jpeg',
        'blog_images/blog10.jpeg'
    ];

    function getRandomImage() {
        const randomIndex = Math.floor(Math.random() * blogImages.length);
        return blogImages[randomIndex];
    }

    // Fetch and display blogs
    function fetchBlogs() {
        fetch('http://127.0.0.1:5000/api/blogs')
            .then(res => res.json())
            .then(blogs => {
                const blogList = document.getElementById('blog-list');
                if (!blogList) return;
                blogList.innerHTML = '';
                if (blogs.length === 0) {
                    blogList.innerHTML = '<p style="text-align:center;color:#888;">No blog posts yet.</p>';
                    return;
                }
                blogs.forEach(blog => {
                    const blogDiv = document.createElement('div');
                    blogDiv.className = 'blog-card';
                    const randomImage = getRandomImage();
                    blogDiv.innerHTML = `
                        <img class="blog-card-image" src="${randomImage}" alt="Blog image" />
                        <div class="blog-card-content">
                            <div class="blog-title">${blog.title}</div>
                            <div class="blog-meta">By ${blog.author} | ${new Date(blog.created_at).toLocaleString('en-US', { timeZone: 'Asia/Kolkata' })}</div>
                            <div class="blog-content">${blog.content}</div>
                        </div>
                    `;
                    blogList.appendChild(blogDiv);
                });
            });
    }

    // Handle blog post creation
    const blogForm = document.getElementById('blog-form');
    if (blogForm) {
        blogForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const title = document.getElementById('blog-title').value;
            const author = document.getElementById('blog-author').value;
            const content = document.getElementById('blog-content').value;
            fetch('http://127.0.0.1:5000/api/blogs', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title, author, content })
            })
            .then(res => res.json())
            .then(() => {
                blogForm.reset();
                fetchBlogs();
            });
        });
    }

    // Move the form below the blog list
    const blogList = document.getElementById('blog-list');
    const addBlogCard = document.querySelector('.add-blog-card');
    if (blogList && addBlogCard) {
        blogList.parentNode.insertBefore(addBlogCard, blogList.nextSibling);
    }

    // Initial fetch
    fetchBlogs();
}); 