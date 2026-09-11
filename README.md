# Python Backend API

A simple Flask REST API with SQLite storage, token-protected write access, and a static HTML client for testing.

## Features

- User registration and login (SHA-256 hashed passwords)
- SQLite database, auto-initialized on startup
- Product listing (public) and product creation (token-protected)
- CORS enabled for browser-based clients
- Free deployment on Render via Gunicorn

## What's inside

- `app.py` — Flask app and all API routes
- `web_client.html` — static HTML/JS page for exercising the API in a browser
- `products.db` — SQLite database file (created automatically)
- `requirements.txt` — Python dependencies
- `Procfile` — Gunicorn start command for Render

## API Endpoints

| Method | Path        | Auth required | Description                          |
|--------|-------------|----------------|--------------------------------------|
| GET    | `/`         | No             | Health check message                 |
| GET    | `/init`     | No             | Create `products` and `users` tables |
| GET    | `/products` | No             | List all products                    |
| POST   | `/products` | Yes (Bearer)   | Add a new product (`name`, `price`)  |
| POST   | `/register` | No             | Register a new user (`username`, `password`) |
| POST   | `/login`    | No             | Log in with `username`, `password`   |

Protected endpoints require an `Authorization: Bearer <API_TOKEN>` header, where `API_TOKEN` matches the value set in your environment.

## How to run locally

1. Clone the repo:
   ```bash
   git clone https://github.com/shbe12/Python-Backend-Flask.git
   cd Python-Backend-Flask
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your API token:
   ```
   API_TOKEN=your-secret-token
   ```

5. Run the server:
   ```bash
   python app.py
   ```

   The API will be available at `http://127.0.0.1:5000`. The database and tables are created automatically on startup.

6. Open `web_client.html` in a browser to try the API (update `BASE_URL` in the script if testing against a local server instead of the deployed one).

## Testing

The API was tested using [Postman](https://www.postman.com/) to verify each endpoint (`/register`, `/login`, `/products`), including the token-protected `POST /products` route with the `Authorization: Bearer <API_TOKEN>` header.

## Deployment

This project is configured for deployment on [Render](https://render.com) using Gunicorn (see `Procfile`). Set the `API_TOKEN` environment variable in your Render dashboard before deploying.
