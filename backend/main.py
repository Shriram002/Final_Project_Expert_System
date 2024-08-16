import uvicorn
from backend_app.api import app  # Import from the backend_app module

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
