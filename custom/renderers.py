import json
from datetime import date, datetime
from typing import Any

from molten import Response
from molten.validation import dump_schema, is_schema

from .animal_case.convert import parse_keys


class JSONRenderer:
    """A JSON response renderer.
    """

    mime_type = "application/json"

    def can_render_response(self, accept: str) -> bool:
        return accept.startswith("application/json")

    def render(self, status: str, response_data: Any) -> Response:
        if response_data is not None:
            try:
                response_data = dump_schema(response_data)
            except TypeError:
                pass
            # TODO - fix hack to prevent camel casing openAPI data
            if not response_data.get('openapi'):
                response_data = parse_keys(response_data, types='camel')
        content = json.dumps(response_data, default=self.default)
        return Response(status, content=content, headers={
            "content-type": "application/json; charset=utf-8",
        })

    def default(self, ob: Any) -> Any:
        """You may override this when subclassing the JSON renderer in
        order to encode non-standard object types.
        """

        if isinstance(ob, (datetime, date)):
            return ob.isoformat()
        if is_schema(type(ob)):
            return dump_schema(ob)
        raise TypeError(f"cannot encode values of type {type(ob)}")  # pragma: no cover
