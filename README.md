# $$\textcolor{red}{\text{UNDER CONSTRUCTION}}$$

# Project Title:

URL Shortener With FastAPI and Python


## 1. What is the project?

In this tutorial, you’ll build a URL shortener with Python and FastAPI. URLs can be extremely long and not user-friendly. This is where a URL shortener can come in handy. A URL shortener reduces the number of characters in a URL, making it easier to read, remember, and share.

At the end of this tutorial, you’ll have a fully functional API-driven web app that creates shortened URLs that forward to target URLs.


## 2. Tech Stack:

- Python 3
- FastAPI
- SQLite
- SQLAlchemy
- Uvicorn

## 3. Dependencies:
 - Installation(s)
```
(venv) $ python -m pip install fastapi==0.75.0 uvicorn==0.17.6
(venv) $ python -m pip install sqlalchemy==1.4.32
(venv) $ python -m pip install python-dotenv==0.19.2
(venv) $ python -m pip install validators==0.18.2
```

- .env file

```
ENV_NAME="XXXXXXXX"
BASE_URL="http://127.0.0.1:XXXX"
DB_URL="sqlite:///./XXXXXXXXXX.db"
```

How To:

- Run the live server using uvicorn:
```commandline
(venv) $ uvicorn shortener_app.main:app --reload
```

## 3. What is the MVP?
The minimal viable product is a REST API driven web application that allow users to create shortened URLs that forward to target URLs.


## 4. What are the sprinkles? 


## 5. When will the project be complete? 
The project will be complete once all the MVP features have been implemented.

## 6. Licence:

## 7. Original Creator:

Author: Philipp Acsany

URL: https://realpython.com/build-a-python-url-shortener-with-fastapi/#demo-your-python-url-shortener

Date: 18 May, 2022
