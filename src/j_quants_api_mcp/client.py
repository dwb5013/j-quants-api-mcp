import os
from functools import lru_cache

from jquantsapi import ClientV2


@lru_cache(maxsize=1)
def get_client() -> ClientV2:
    api_key = os.environ.get("JQUANTS_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "JQUANTS_API_KEY environment variable is not set. "
            "Get your API key from https://application.jpx-jquants.com/"
        )
    return ClientV2(api_key=api_key)
