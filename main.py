import uvicorn

from core import config

if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host=config.DB_HOST,
        port=3228,
        reload=True
    )
