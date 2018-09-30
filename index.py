from typing import List, Union

from molten import (
    App, Component, ResponseRendererMiddleware, Middleware, SettingsComponent
)
from molten import Route, Include
from molten import URLEncodingParser, MultiPartParser
from molten.contrib.sqlalchemy import (
    SQLAlchemyEngineComponent, SQLAlchemyMiddleware,
    SQLAlchemySessionComponent, EngineData)
from molten.openapi import HTTPSecurityScheme, Metadata, OpenAPIHandler, OpenAPIUIHandler

from api.comment.views import list_comments, create_comment, get_comment, delete_comment
from api.user.views import list_users, create_user, get_user, delete_user
from custom import JSONParser, JSONRenderer
from db import Base
import settings


get_docs = OpenAPIUIHandler()

get_schema = OpenAPIHandler(
    metadata=Metadata(
        title="Molten-Boilerplate API",
        description="An API for Molten-Boilerplate.",
        version="0.0.0",
    ),
    security_schemes=[
        HTTPSecurityScheme("default", "bearer"),
    ],
    default_security_scheme="default",
)

components: List[Component] = [
    # TOMLSettingsComponent(),
    SQLAlchemyEngineComponent(),
    SQLAlchemySessionComponent(),
    SettingsComponent(settings.SETTINGS)
]

middleware: List[Middleware] = [
    ResponseRendererMiddleware(),
    SQLAlchemyMiddleware(),
]

routes: List[Union[Route, Include]] = [
    Include("/api/v1/users", [
        Route("", list_users),
        Route("", create_user, method="POST"),
        Route("/{user_id}", delete_user, method="DELETE"),
        Route("/{user_id}", get_user),
    ]),

    Include("/api/v1/comments", [
        Route("", list_comments),
        Route("", create_comment, method="POST"),
        Route("/{comment_id}", delete_comment, method="DELETE"),
        Route("/{comment_id}", get_comment),
    ]),

    Route("/_docs", get_docs),
    Route("/_schema", get_schema),
]


def init_db(engine_data: EngineData):
    Base.metadata.create_all(engine_data.engine)


def setup_db(app):
    # Initialize the DB by injecting EngineData into init_db and calling it.
    resolver = app.injector.get_resolver()
    resolver.resolve(init_db)()


def create_app(_components=None, _middleware=None, _routes=None):
    app = App(
        components=_components or components,
        middleware=_middleware or middleware,
        routes=_routes or routes,
        parsers=[
            JSONParser(),
            URLEncodingParser(),
            MultiPartParser(),
        ],
        renderers=[JSONRenderer()]
    )
    setup_db(app)
    return app
