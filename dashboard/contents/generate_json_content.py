from typing import Any

from contents.models import Content


def generate_json_content() -> dict[str, Any]:
    content = Content.objects.last()
    return content.json if content else {}
