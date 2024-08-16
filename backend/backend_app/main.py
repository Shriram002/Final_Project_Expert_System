import sys
import os
import uvicorn

# Add the root directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend_app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
