import logging

from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException

from utils import get_comments_by_post_id, get_posts_all, search_for_posts, get_posts_by_user, get_post_by_pk

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
logging.basicConfig(filename="api.log", level=logging.INFO)
console_handler = logging.StreamHandler()
formatter_one = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
console_handler.setFormatter(formatter_one)
api_logging = logging.getLogger("api")
api_logging.addHandler(console_handler)
api_logging.info("Логгер api работает")


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
    return render_template('user-feed.html', posts_user=posts_user, user_name=username)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e

    return render_template('500_generic.html', e=e), 500


@app.route('/api/posts')
def take_json_list():
    api_logging.info('Запрос /api/posts')
    return get_posts_all()


@app.route('/api/posts/<post_id>')
def take_json_list_by_id(post_id):
    api_logging.info(f'Запрос /api/posts/{post_id}')
    return get_post_by_pk(post_id)


if __name__ == "__main__":
    app.run()
