from fastapi import FastAPI
from fastapi_users import router

from core import config
from core.imports.routes_import import routes
from core.middleware.cors import init_cors


def create_app():
    _app = FastAPI(
        title='My first application',
        docs_url='/docs'
    )
    return _app

app = create_app()

app.include_router(routes)
init_cors(app)

@app.on_event("startup")
async def startup_event():
    print(f'INFO:     docs - http://{config.APP_HOST}:{config.APP_PORT}/docs')