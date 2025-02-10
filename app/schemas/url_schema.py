from pydantic import BaseModel, HttpUrl


class UrlCreateModel(BaseModel):
    long_url: HttpUrl


class UrlResponseModel(BaseModel):
    short_url: str
