from pydantic import HttpUrl
from sqlalchemy.orm import Session
from app.models.url_models import Url
from app.core.config import settings
import random, string


class UrlService:
    @staticmethod
    def generate_short_code(length=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @classmethod
    def create_short_url(cls, session: Session, long_url: HttpUrl) -> dict:
        existing_url = session.query(Url).filter(Url.long_url == str(long_url)).first()
        if existing_url:
            short_url = f"{settings.base_url}/{existing_url.short_code}"
            return {"short_url": short_url}
        short_code = cls.generate_short_code()
        new_url = Url(long_url=str(long_url), short_code=short_code)
        session.add(new_url)
        session.commit()
        session.refresh(new_url)
        short_url = f"{settings.base_url}/{short_code}"
        return {"short_url": short_url}

    @staticmethod
    def get_long_url(session: Session, short_code: str):
        return session.query(Url).filter(
            Url.short_code == short_code
        ).first()
