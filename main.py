import uvicorn

from core import config

if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host='0.0.0.0',
        port=8200,
        reload=True
    )
