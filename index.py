from typing import List, Union

from molten import (
    App, Component, Include,
    ResponseRendererMiddleware, Route, Middleware
)
from molten.contrib.sqlalchemy import (
    SQLAlchemyEngineComponent, SQLAlchemyMiddleware,
    SQLAlchemySessionComponent
)
from molten.contrib.toml_settings import TOMLSettingsComponent
from molten.openapi import HTTPSecurityScheme, Metadata, OpenAPIHandler, OpenAPIUIHandler

from api.user.views import list_users, create_user, get_user
from db import setup_db

get_docs = OpenAPIUIHandler()

get_schema = OpenAPIHandler(
    metadata=Metadata(
        title="Grant API",
        description="An API for Grant.io.",
        version="0.0.0",
    ),
    security_schemes=[
        HTTPSecurityScheme("default", "bearer"),
    ],
    default_security_scheme="default",
)

routes: List[Union[Route, Include]] = [
    Include("/v1/users", [
        Route("", list_users),
        Route("", create_user, method="POST"),
        Route("/{user_id}", get_user),
    ]),

    Route("/_docs", get_docs),
    Route("/_schema", get_schema),
]

components: List[Component] = [
    TOMLSettingsComponent(),
    SQLAlchemyEngineComponent(),
    SQLAlchemySessionComponent(),
]

middleware: List[Middleware] = [
    ResponseRendererMiddleware(),
    SQLAlchemyMiddleware(),
]


def create_app(_components=False, _middleware=False, _routes=False, _setup_db=True):
    app = App(
        components=_components or components,
        middleware=_middleware or middleware,
        routes=_routes or routes,
    )

    if _setup_db:
        setup_db(app)
    return app
