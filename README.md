# Library API

A simple RESTful API for managing a library system built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**.

## Features

* Register and authenticate librarians and readers
* Add, update, delete, and view books
* Issue and return books
* Business rules:

  * A book can be borrowed only if available (`amount > 0`)
  * A reader can borrow up to 3 books
  * A book cannot be returned if it wasn't borrowed or already returned

## Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic (migrations) - (WIP)
* Pytest (for tests) - (WIP)

## Getting Started

1. **Clone repo**
   `git clone https://github.com/your-username/library-api`

2. **Install dependencies**
   `pip install -r requirements.txt`

3. **Set up `.env`**
   Add database URL, secret key, etc.

4. **Start the app**
   `uvicorn app.main:app --reload`

5. **API docs**
   Go to: `http://localhost:8000/docs`

