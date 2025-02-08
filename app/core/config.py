from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    environment: str = None
    version: str = None


class TinyUrlSettings(Settings):
    api_url_prefix: str = None
    database_url: str = None

    model_config = SettingsConfigDict(env_file='.env')

settings = TinyUrlSettings()
