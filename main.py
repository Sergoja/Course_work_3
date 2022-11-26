from flask import Flask, render_template, request
from utils import get_comments_by_post_id, get_posts_all, search_for_posts, get_posts_by_user

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
    word_search = request.args['word_search']
    find_posts = search_for_posts(word_search)
    return render_template('search.html', find_posts=find_posts, word_search=word_search)


@app.route('/users/<username>')
def user_feed_page(username):
    posts_user = get_posts_by_user(username)
    return render_template('user-feed.html', posts_user=posts_user)


# @app.route('/<non_page>')
# def error_page(non_page):
#

app.run()
