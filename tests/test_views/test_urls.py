import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from tests.config import client
from app.core.config import get_session
from app.schemas.url_schema import UrlCreateModel
from app.services.url_service import UrlService


@pytest.fixture(scope="function")
def session():
    db_generator = get_session()
    db = next(db_generator)
    try:
        yield db
    finally:
        next(db_generator, None)


@pytest.fixture(scope="function")
def test_url(session: Session):
    url_data = UrlCreateModel(long_url="https://example.com")
    short_url = UrlService.create_short_url(session, long_url=url_data.long_url)
    session.commit()
    return short_url


def test_create_short_url(session: Session):
    response = client.post("/create", json={
        "user_id": 1,
        "long_url": "https://newexample.com"
    })
    assert response.status_code == 201
    assert "short_url" in response.json()


def test_redirect_to_long_url(session: Session, test_url):
    response = client.get(f"/{test_url.short_url}")
    assert response.status_code == 200
    assert response.url == test_url.long_url


def test_update_short_url(session: Session, test_url):
    response = client.put(f"/{test_url.short_url}", json={
        "user_id": 1,
        "short_url": test_url.short_url,
        "long_url": "https://updatedexample.com"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Short URL updated successfully"


def test_delete_short_url(session: Session, test_url):
    response = client.delete(f"/{test_url.short_url}", json={
        "user_id": 1,
        "short_code": test_url.short_url
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Short URL deleted successfully"
