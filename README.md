## API BDD Testing PoC Project
This Project is a PoC for BDD approach of testing API using Python Behave and httpx libraries.
Also for response validation, I have used pydantic library.

### Project structure
Given project structure allows us to separate the feature files, step definitions, and the API client code.

In the `helpers` directory, we have the `basic_api_helper.py` and `movie_api_helper.py` file that contains the API client code. This code is used to make the API requests.

In the `models` directory, we have the `movie_search_model.py` file that contains the Pydantic model for the movie object. It allows us to validate responses from the API. We can validate types, values, and the structure of the response.

In the `tests` directory, we have the `features` directory that contains the feature files and the `steps` directory that contains the step definitions. The feature files are written in Gherkin language and contain the scenarios that we want to test. The step definitions are written in Python and contain the code that is executed when a step is matched.

All tests can be parametrized and run in parallel.

Moreover all helpers and models can be used in other projects as well as a python package.

## Installation
To install the project, you need to have Python 3.11 or higher installed on your machine. You can install the project by following these steps:

1. Install Poetry by running the following command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
2. Activate the virtual environment by running the following command:
```bash
poetry shell
```
3. Install the project dependencies by running the following command:
```bash
poetry install
```
4. Run the tests by running the following command:
```bash
behave
```