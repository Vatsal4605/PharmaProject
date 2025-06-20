from flask import Blueprint, request, jsonify
from models import Blog, db
from datetime import datetime
import pytz

blog_api = Blueprint('blog_api', __name__)

@blog_api.route('/api/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return jsonify([{
        'id': b.id,
        'title': b.title,
        'content': b.content,
        'author': b.author,
        'created_at': b.created_at.isoformat()
    } for b in blogs])

@blog_api.route('/api/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return jsonify({
        'id': blog.id,
        'title': blog.title,
        'content': blog.content,
        'author': blog.author,
        'created_at': blog.created_at.isoformat()
    })

@blog_api.route('/api/blogs', methods=['POST'])
def create_blog():
    data = request.get_json()
    blog = Blog(
        title=data.get('title'),
        content=data.get('content'),
        author=data.get('author', 'Anonymous'),
        created_at=datetime.now(pytz.timezone('Asia/Kolkata'))
    )
    db.session.add(blog)
    db.session.commit()
    return jsonify({'message': 'Blog post created!', 'id': blog.id}), 201

@blog_api.route('/api/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    data = request.get_json()
    blog.title = data.get('title', blog.title)
    blog.content = data.get('content', blog.content)
    blog.author = data.get('author', blog.author)
    db.session.commit()
    return jsonify({'message': 'Blog post updated!'})

@blog_api.route('/api/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'message': 'Blog post deleted!'}) 