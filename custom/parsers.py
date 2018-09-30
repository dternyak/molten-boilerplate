import json
from typing import Any

from molten import RequestBody
from molten.errors import ParseError

from .animal_case.convert import parse_keys


class JSONParser:
    """A JSON request parser.
    """

    mime_type = "application/json"

    def can_parse_content(self, content_type: str) -> bool:
        return content_type.startswith("application/json")

    def parse(self, data: RequestBody) -> Any:
        try:
            return parse_keys(json.loads(data))
        except json.JSONDecodeError:
            raise ParseError("JSON input could not be parsed")
