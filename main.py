"""A very basic FastAPI app.

Run it with:
    uvicorn main:app --reload
Then open http://127.0.0.1:8000/docs for the interactive docs.
"""

from fastapi import FastAPI

# The FastAPI "app" object. Uvicorn looks for this by name (main:app).
app = FastAPI(
    title="Basic FastAPI App",
    description="My first small API: a welcome endpoint and a greeting endpoint.",
    version="1.0.0",
)


@app.get("/", summary="Welcome message")
def read_root():
    """Return a simple welcome message so you know the API is running."""
    return {
        "message": "Welcome to my first FastAPI app!",
        "docs": "/docs",
    }


@app.get("/greet/{name}", summary="Greet someone by name")
def greet(name: str, greeting: str = "Hello"):
    """Greet a person.

    - **name** (path parameter, required): who to greet, taken from the URL.
    - **greeting** (query parameter, optional): the word to use. Defaults to "Hello".

    Example: /greet/Suresh?greeting=Hi
    """
    return {
        "name": name,
        "greeting": greeting,
        "message": f"{greeting}, {name}!",
    }
