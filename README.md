# HNG12 Stage 1 Task

## Project Description

This is a public API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Setup Instructions

1. Clone the repository:

    ```sh
    git clone https://github.com/samadeolu7/hng-stage-1-task.git
    cd hng-stage-1-task
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv my_env
    my_env\Scripts\activate  # On Windows
    source my_env/bin/activate  # On Unix or MacOS
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:

    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
    ```

## API Documentation

### Endpoint URL

`GET /api/classify-number?number={number}`

### Request/Response Format

#### Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Response (400 Bad Request)

```json
{
    "number": "invalid",
    "error": true
}
```

## Example Usage

```sh
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
```

## Backlink

[Backlink to HNG python](https://hng.tech/hire/python-developers)