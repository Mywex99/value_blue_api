from typing import Any

from helpers.basic_api_helper import BasicHTTPApi

headers = {"Content-Type": "application/json"}


class MovieAPI(BasicHTTPApi):
    """
    Base class for Movie API.
    Here considered all needed HTTP interfaces
    to work with Movie API
    """

    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.base_url = url
    
    def get_search(self, querystring) -> tuple[Any, Any]:
        """
        Get search results
        :return: search results
        """

        headers = {
	        "X-RapidAPI-Key": "f5e5be9a22msh2e724bb87e58246p1fbb51jsn1396b4b02ebb",
	        "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
        }
        
        code, result = self.call_api(self.base_url, headers=headers, parameters=querystring)
        return code, result
