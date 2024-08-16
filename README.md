
# Supply Chain Optimization System

This project is an expert system designed to optimize supply chain management by automating decision-making related to inventory management, supplier selection, and transportation logistics.

## Project Structure

- `backend/`: Contains the FastAPI backend code.
- `frontend/`: Contains the Streamlit frontend code.
- `test/`: Contains test cases for the backend logic and API.

## Running the Project

### Backend
1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI server:
    ```bash
    python app/main.py
    ```

### Frontend
1. Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Testing
1. Navigate to the `test` directory:
    ```bash
    cd test
    ```
2. Run the test cases:
    ```bash
    pytest
    ```

## Docker
To run the application using Docker, you can use the provided Dockerfiles in both the `backend` and `frontend` directories.

### Backend
```bash
cd backend
docker build -t supply-chain-backend .
docker run -p 8000:8000 supply-chain-backend
```

### Frontend
```bash
cd frontend
docker build -t supply-chain-frontend .
docker run -p 8501:8501 supply-chain-frontend
```

## Adding a Collaborators Tab

You can add a "Collaborators" tab to the Streamlit app by following these steps:

```python
import streamlit as st

# Set up tabs
tabs = st.tabs(["Home", "Inventory", "Supplier Selection", "Logistics", "Collaborators"])

# Collaborators Tab
with tabs[4]:
    st.header("Collaborators")
    st.write("This project is developed by:")
    st.write("- Manarth Patel")
    st.write("- Shriram Yadav")
    st.write("- Rakshay Patel")
```

## Enhancing the UI with Fancy Elements

### Adding a Line Chart
```python
import pandas as pd
import numpy as np
import streamlit as st

# Sample data
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['Inventory Level', 'Supplier Efficiency', 'Logistics Cost']
)

# Line chart
st.line_chart(data)
```

### Adding a Progress Bar
```python
import time
import streamlit as st

st.header("Optimizing Supply Chain...")

progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i + 1)

st.write("Optimization Complete!")
```

### Docker Compose Setup
You can combine the backend and frontend into a single Docker Compose setup.

#### Example `docker-compose.yml`:
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
```