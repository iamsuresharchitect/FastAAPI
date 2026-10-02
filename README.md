# Basic FastAPI App

A first, small web API built with FastAPI and run with Uvicorn.

## Endpoints

| Method | URL | What it returns |
|---|---|---|
| GET | `/` | A welcome message |
| GET | `/greet/{name}` | A greeting for `name` (path parameter) |
| GET | `/greet/{name}?greeting=Hi` | Same, with a custom greeting (optional query parameter, defaults to `Hello`) |
| GET | `/docs` | Interactive API docs (Swagger UI), generated automatically |

## Setup (one time)

```bash
cd fastapi-basic
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate          # macOS / Linux
# venv\Scripts\activate           # Windows (PowerShell or cmd)

pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

`main:app` means "the `app` object inside `main.py`". `--reload` restarts the server whenever you save the file.

Then open in your browser:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/greet/Suresh
- http://127.0.0.1:8000/greet/Suresh?greeting=Hi
- http://127.0.0.1:8000/docs  (click an endpoint, then "Try it out", then "Execute")

Stop the server with `Ctrl+C`. Leave the venv with `deactivate`.

## What happens with missing values

- `/greet/Suresh` with no `greeting` uses the default `Hello`.
- `/greet/` with no name returns `404 Not Found`, because `name` is a required part of the path.
