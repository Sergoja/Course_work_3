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




# get_posts_by_user(user_name) – возвращает посты определенного пользователя.
# Функция должна вызывать ошибку ValueError если такого пользователя нет и пустой список,
# если у пользователя нет постов.

# get_comments_by_post_id(post_id) – возвращает комментарии определенного поста.
# Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у поста нет комментов.

# search_for_posts(query) – возвращает список постов по ключевому слову

# get_post_by_pk(pk) – возвращает один пост по его идентификатору.
