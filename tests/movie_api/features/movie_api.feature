Feature: Movie API

    Scenario: GET By Search
        Given a movie API
        When a GET request is made to API with query parameter "search"
        Then the API should return a list of movies matching the search query

    Scenario: GET By ID or Title
        Given a movie API
        When a GET request is made to "/movies/{idOrTitle}"
        Then the API should return the movie with the specified ID or title

    Scenario: Create a Movie
        Given a movie API
        When a POST request is made to "/movies" with the movie details
        Then the API should create a new movie and return its ID

    Scenario: Update a Movie
        Given a movie API
        When a PUT request is made to "/movies/{id}" with the updated movie details
        Then the API should update the movie with the specified ID

    Scenario: Delete a Movie
        Given a movie API
        When a DELETE request is made to "/movies/{id}"
        Then the API should delete the movie with the specified ID
