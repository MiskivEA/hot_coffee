import uvicorn
from fastapi import FastAPI
from app.database import create_db_and_tables
import asyncio

app = FastAPI()
asyncio.run(create_db_and_tables())


@app.get('/')
async def hello(user: str = 'User'):

    return {'message': f'Hello {user}'}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='localhost')
