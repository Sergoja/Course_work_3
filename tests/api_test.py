import pytest

from utils import get_posts_all, get_post_by_pk


def test_get_posts_all():
    assert type(get_posts_all()) == list


expected_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']


def test_keys_in_load_posts():
    for post in get_posts_all():
        keys = [key for key in post.keys()]
        assert keys == expected_keys


def test_get_post_by_pk():
    for i in range(1, 8):
        assert type(get_post_by_pk()) == dict


def test_keys_in_get_post_by_pk():
    for i in range(1, 8):
        keys = [key for key in get_post_by_pk(i).keys()]
                assert keys == expected_keys
