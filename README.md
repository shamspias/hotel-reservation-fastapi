# FastAPI Hotel Reservation System

## Overview
This project is a simple FastAPI application for managing hotel reservations. It allows for creating, retrieving, and managing hotel reservations.

## Installation

### Requirements
- Python 3.7+
- Pip

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/shamspias/hotel-reservation-fastapi
   cd hotel-reservation-fastapi
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

### Endpoints

#### 1. Create Reservation
- **POST** `/reservations/`
- **Description**: Create a new hotel reservation.
- **Body**:
  - `number_of_people`: Integer
  - `full_name`: String
  - `email`: String
  - `phone_number`: String
  - `address`: String
  - `payment_card_info`: String (Note: For real applications, use a secure payment gateway)
  - `stay_duration`: Integer
  - `room_type`: String (e.g., 'single', 'double', 'suite')

#### 2. Read Reservations
- **GET** `/reservations/`
- **Description**: Retrieve a list of all reservations.
- **Query Parameters**:
  - `skip`: Integer (optional)
  - `limit`: Integer (optional)

#### 3. Read Single Reservation
- **GET** `/reservations/{reservation_id}`
- **Description**: Retrieve details of a specific reservation.
- **Path Parameters**:
  - `reservation_id`: Integer

### Example Usage

Request:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/reservations/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "number_of_people": 2,
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "phone_number": "123-456-7890",
  "address": "123 Main St, Anytown, AT 12345",
  "payment_card_info": "1234567890123456, 12/25, 123",
  "stay_duration": 5,
  "room_type": "double"
}'
```

Response:

```json
{
  "id": 1,
  "number_of_people": 2,
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "phone_number": "123-456-7890",
  "address": "123 Main St, Anytown, AT 12345",
  "payment_card_info": "1234567890123456, 12/25, 123",
  "stay_duration": 5,
  "room_type": "double"
}
```

## Security and Improvements

- **Security**: For handling payment information, integrate with a secure payment gateway. Do not store sensitive payment details directly in the database.
- **Authentication**: Implement user authentication and authorization for better security.
- **Database**: For production, consider using a more robust database system like PostgreSQL.
- **Error Handling**: Improve error handling for a more resilient application.
- **Testing**: Add unit and integration tests.

---
