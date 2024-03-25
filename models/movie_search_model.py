from __future__ import annotations

from typing import List

from pydantic import BaseModel


class SearchItem(BaseModel):
    Title: str
    Year: str
    imdbID: str
    Type: str
    Poster: str


class MovieSearchModel(BaseModel):
    Search: List[SearchItem]
    totalResults: str
    Response: bool