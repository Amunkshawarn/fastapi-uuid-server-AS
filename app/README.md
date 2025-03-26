### 1️⃣ Prerequisites

- Python 3.11.0
- Poetry (for dependency management)
- Docker (for containerization)

### 2️⃣ Clone the Repository

git clone <repository_url>
cd fastapi-uuid-server/app

### 3️⃣ Install Dependencies

install all required dependencies:

```sh
poetry install
```

### 4️⃣ Run the Server Locally

To start the FastAPI server, run:

```sh
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```

### 5️⃣ Test the API

After starting the server, you can test the endpoints:

- Open your browser and visit:
  - **Swagger UI:** [http://localhost:8000/docs]

### 6️⃣ Run the Server using Docker

To build and run the server inside a Docker container:

1. **Build the Docker image:**
   ```sh
   docker build -t fastapi-uuid-server .
   ```
2. **Run the container:**
   ```sh
   docker run -p 8000:8000 fastapi-uuid-server
   ```

### 7️⃣ API Endpoints

| Endpoint      | Method | Description                      |
| ------------- | ------ | -------------------------------- |
| `/uuid`       | GET    | Generates a UUID                 |
| `/async-uuid` | GET    | Generates a UUID with a 3s delay |
| `/cat`        | GET    | Fetches a random cat image       |

### 8️⃣ Stop the Server

- `CTRL+C` to stop the server.
- If running via Docker, find the container ID using:
  ```sh
  docker ps
  ```
  Then stop it using:
  ```sh
  docker stop <container_id>
  ```
