from behave import given, when, then

import pytest

from helpers import MovieAPI
from models import MovieSearchModel

movie_api_rest: MovieAPI = MovieAPI("https://movie-database-alternative.p.rapidapi.com") 

@pytest.fixture
def context():
    b = None
    yield b

@given('a movie API')
async def step_impl(context):
    print('Starting browser')
    pass

@when('a GET request is made to API with query parameter "search"')
def test_search_movie_api(context):
    querystring = {"s":"Avengers Endgame","r":"json","page":"1"}
    context.code, context.result = movie_api_rest.get_search(querystring)
    assert context.code == 200

@then('the API should return a list of movies matching the search query')
def test_search_movie_api_response(context):
    assert context.code == 200
    assert MovieSearchModel.model_validate(context.result)

# Rest CRUD scenarios for other movie API endpoints can be added below according to the same pattern
# or can be separated into different files for better organization