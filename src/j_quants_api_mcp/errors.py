import json
import traceback

from requests.exceptions import HTTPError


def format_error(e: Exception, method: str) -> str:
    if isinstance(e, RuntimeError) and "JQUANTS_API_KEY" in str(e):
        return json.dumps({
            "error": "auth_error",
            "message": str(e),
            "method": method,
        }, ensure_ascii=False)

    if isinstance(e, HTTPError):
        status = e.response.status_code if e.response is not None else None
        hint = ""
        if status == 403:
            hint = "This endpoint may require a higher subscription plan."
        elif status == 400:
            hint = "Check parameter format. Dates should be YYYYMMDD."
        elif status == 429:
            hint = "Rate limit exceeded. Try again later or reduce request frequency."

        return json.dumps({
            "error": "api_error",
            "status_code": status,
            "message": str(e),
            "hint": hint,
            "method": method,
        }, ensure_ascii=False)

    return json.dumps({
        "error": "unexpected_error",
        "message": str(e),
        "traceback": traceback.format_exc(),
        "method": method,
    }, ensure_ascii=False)
