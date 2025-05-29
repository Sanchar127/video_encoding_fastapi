

import tracemalloc
from fastapi import FastAPI, Response, Request, Depends
# from fastapi.openapi.utils import get_open

from fastapi.openapi.docs import get_swagger_ui_html

# from fastapi.staticfiles import StaticFiles
# from project.template import templates

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi_redis_cache import FastApiRedisCache

from project.routes.base import api_router

from project.config import settings

from fastapi_pagination import add_pagination
from project.config import settings


origins=["*"]


def create_app() -> FastAPI:
	app = FastAPI(
		title=settings.PROJECT_NAME,
		version=settings.PROJECT_VERSION,
		debug=settings.APP_DEBUG,
		# openapi_url="/v1/docs/api-docs" if settings.APP_ENV == "dev" or settings.APP_ENV == "test" else None,
		# docs_url="/v1/xxyz/docs/project" if settings.APP_ENV == "dev" or settings.APP_ENV == "test" else None,
		# redoc_url="/v1/xxyz/redoc" if settings.APP_ENV == "dev" or settings.APP_ENV == "test" else None,
	)

	tracemalloc.start()

	app.add_middleware(TrustedHostMiddleware, allowed_hosts=origins)

	app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

	app.add_middleware(
		CORSMiddleware,
		allow_origins=origins,
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)



	
	@app.on_event('startup')
	def startup():
		redis_cache = FastApiRedisCache()
		redis_cache.init(
			host_url=settings.REDIS_URL,
			prefix="Appsettings-cache",
			response_header="X-AppSettings-Cache",
			ignore_arg_types=[Request, Response, Session]
		)

	app.include_router(api_router)
	add_pagination(app)

	# @app.get("/openapi.json", name="openapijson", include_in_schema=False)
	# async def get_open_api_endpoint(current_user: Admin = Depends(get_admin_user)):
	# 	return JSONResponse(get_openapi(title=app.title, version=app.version, routes=app.routes))

	# @app.get("/docs", name="documentation", include_in_schema=False)
	# async def get_documentation(request: Request, current_user: Admin = Depends(get_admin_user)):
	# 	return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

	return app

app = create_app()