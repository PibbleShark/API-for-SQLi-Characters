import random

from app import app
from flask import json

from sql_chars import sanitize_check
from char_list import char_list


def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_post():
    # adapted from tutorial at https://riptutorial.com/flask/example/5622/testing-a-json-api-implemented-in-flask
    response = app.test_client().post('/v1/sanitized/input/',
                                      data=json.dumps({
                                          "payload": "input"}),
                                      content_type='application/json',
                                      )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['result'] == 'sanitized'


def test_sanitize_check():
    unsanitized = sanitize_check(random.choice(char_list))
    assert unsanitized == 'unsanitized'
