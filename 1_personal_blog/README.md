# Personal Blog

A minimal, customizable personal blog project with functionality of creating Users and Posts and performing CRUD operations on them


## Tech
- Python 3.11
- mongoengine
- MongoDB
- pydantic
- FastAPI

## Getting started
- 1. Create .env file in /backend folder
- 2. Setup MongoDB Server and add MONGODB_URL in .env file
- 3. Create virtual env and install all the dependencies
- 4. Run the following command to start the server
  
    ```
        uvicorn main:app --reload
    ```
