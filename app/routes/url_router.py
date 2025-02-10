from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import RedirectResponse
from urllib.parse import urlparse
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.schemas.url_schema import (UrlCreateModel, UrlResponseModel)
from app.core.config import get_session
from app.services.url_service import UrlService

url_router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
@url_router.post(
    "/shorten",
    tags=['Shorten Url'],
    summary='Create a new short url',
    status_code=status.HTTP_201_CREATED,
    response_model=UrlResponseModel,
)
@limiter.limit("10/minute")
async def root(
        request: UrlCreateModel,
        session: Session = Depends(get_session)
):
    response = UrlService.create_short_url(session=session, long_url=request.long_url)
    return response


@url_router.get(
    "/{short_code}",
    tags=['Redirect Url'],
    summary='Redirect to long url',
    status_code=status.HTTP_302_FOUND,
)
def redirect_to_long_url(
        short_code: str,
        session: Session = Depends(get_session)
):
    url_entry = UrlService.get_long_url(session=session, short_code=short_code)
    if url_entry is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    parsed_url = urlparse(url_entry.long_url)
    if not parsed_url.scheme:
        long_url = f"https://{url_entry.long_url}"
    else:
        long_url = url_entry.long_url

    return RedirectResponse(long_url)
