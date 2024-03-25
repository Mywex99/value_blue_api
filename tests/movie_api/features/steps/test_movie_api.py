from behave import given, when, then

import pytest

from helpers import MovieAPI
from models import MovieSearchModel


@pytest.fixture
def context():
    b = None
    yield b

@given('a movie API')
async def step_impl(context):
    print('Starting browser')
    pass

@when('a GET request is made to API with query parameter "search"')
def test_search_movie_api(context, movie_api_rest: MovieAPI):
    querystring = {"s":"Avengers Endgame","r":"json","page":"1"}
    context.code, context.result = movie_api_rest.get_search(querystring)
    assert context.code == 200

@then('the API should return a list of movies matching the search query')
def test_search_movie_api_response(context):
    assert context.code == 200
    assert MovieSearchModel.model_validate(context.result)
