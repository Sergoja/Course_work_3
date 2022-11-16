from flask import Flask, render_template
from utils import get_comments_by_post_id, get_posts_all

app = Flask(__name__)


@app.route('/')
def main_page():
    all_posts = get_posts_all()
    return render_template('index.html', all_posts=all_posts)


@app.route('/posts/<int:post_id>')
def post_page(post_id):
    comments_by_post_id = get_comments_by_post_id(post_id)
    all_posts = get_posts_all()
    required_post = {}
    for post in all_posts:
        if int(post['pk']) == int(post_id):
            required_post = post
    return render_template('post.html', comments=comments_by_post_id, required_post=required_post)


@app.route('/search')
def search_page():
    return render_template('search.html')


@app.route('/user-feed')
def user_feed_page():
    return render_template('user-feed.html')


app.run()
