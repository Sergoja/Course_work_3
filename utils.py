import json


def get_posts_all():
    with open("data/posts.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_by_post_id(post_id):
    with open("data/comments.json", 'r', encoding='utf-8') as file:
        comments_by_post_id = []
        for comment in json.load(file):
            if int(comment['post_id']) == int(post_id):
                comments_by_post_id.append(comment)
    return comments_by_post_id


def search_for_posts(query):
    find_posts = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            find_posts.append(post)
    return find_posts


def get_posts_by_user(user_name):
    posts_by_user = []
    for post in get_posts_all():
        if user_name == post['poster_name']:
            posts_by_user.append(post)
    return posts_by_user


# get_posts_by_user(user_name) – возвращает посты определенного пользователя.
# Функция должна вызывать ошибку ValueError если такого пользователя нет и пустой список,
# если у пользователя нет постов.

# get_comments_by_post_id(post_id) – возвращает комментарии определенного поста.
# Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у поста нет комментов.

# get_post_by_pk(pk) – возвращает один пост по его идентификатору.
