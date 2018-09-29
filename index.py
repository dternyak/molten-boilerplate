from typing import List, Union

from molten import (
    App, Component, ResponseRendererMiddleware, Middleware
)
from molten import Route, Include
from molten.contrib.sqlalchemy import (
    SQLAlchemyEngineComponent, SQLAlchemyMiddleware,
    SQLAlchemySessionComponent
)
from molten.contrib.toml_settings import TOMLSettingsComponent
from molten.openapi import HTTPSecurityScheme, Metadata, OpenAPIHandler, OpenAPIUIHandler

from api.user.views import list_users, create_user, get_user, delete_user
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

components: List[Component] = [
    TOMLSettingsComponent(),
    SQLAlchemyEngineComponent(),
    SQLAlchemySessionComponent(),
]

middleware: List[Middleware] = [
    ResponseRendererMiddleware(),
    SQLAlchemyMiddleware(),
]

routes: List[Union[Route, Include]] = [
    Include("/v1/users", [
        Route("", list_users),
        Route("", create_user, method="POST"),
        Route("/{user_id}", delete_user, method="DELETE"),
        Route("/{user_id}", get_user),
    ]),

    Route("/_docs", get_docs),
    Route("/_schema", get_schema),
]


def create_app(_components=None, _middleware=None, _routes=None):
    app = App(
        components=_components or components,
        middleware=_middleware or middleware,
        routes=_routes or routes,
    )

    setup_db(app)
    return app
