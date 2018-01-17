import requests
import random


from app.models.comment import Comment
from app.api_helper import JsonplaceholderRestApi

comments = []
app = JsonplaceholderRestApi


def add_comment(new_comment):
    comments.append(new_comment)


def get_comment():
    return comments.pop()


def create_comment(url, data):
    """primitive method, use the same method from rest-API instead"""

    response = requests.post(url, data=data)
    return response.json()


def clean_up():
    for comment in comments:
        app.remove_comment(comment)


def get_default_comment():
    return Comment(
        str(random.randint(1, 100)),
        str(random.randint(1, 100)),
        'John Snou',
        'test@gmail.com',
        'lorem ipsum dolor sit amet')
