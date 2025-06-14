# Event Management API

## Overview

This API allows users to register for events, track attendance, and manage both event information and speaker details. It supports CRUD operations and enforces simple validation and relationships between the entities. This is for my AltSchool Second Semester exam.

## API Endpoints

- User Endpoints
- Event Endpoints
- Registration Endpoints

## Technical Requirements

- Use **Pydantic models** for validation
- Store data in **in-memory lists or dictionaries**
- Return appropriate **HTTP status codes** for all operations

## Setup

### 1. Backend (FastAPI)

#### Requirements

- Python 3.8+
- [Uvicorn](https://www.uvicorn.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

#### Installation

```bash
cd backend
pip install -r requirements.txt
```

#### Usage

1. Run

```bash
uvicorn main:app --reload
```

2.The API will be live at: **<http://localhost:8000>**
3.Go to **<http://localhost:8000/docs>** to test the API.

## Contirbuting

Feel free to clone and fork this repository. You can also submit pull requests. Any contributions are welcome!

You are also free to customize it further to fit your needs! If you have any specific details you'd like to add or change, let me know.
