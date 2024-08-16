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