# URL Shortener Service

This is a simple URL shortener built with FastAPI and PostgreSQL.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn app.main:app --reload`

## API Endpoints
- **POST /shorten**: Shortens a long URL
- **GET /{short_code}**: Redirects to the original URL
