from typing import Any, Dict, Optional

import requests
from requests import Response

from app.finance_platforms.yahoo_finance.yahoo_finance_constants import (
    YahooFinanceConstants,
)


class RequestUtil:
    """helper functions for sending http requests"""

    @staticmethod
    def get_request(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """

        Args:
            url:
            headers: if None, using default header.
                Apparently sending a request without header will have issues. Need to learn it later
            params:

        Returns:
            Response
        """
        if headers is None:
            headers = {"User-Agent": YahooFinanceConstants.USER_AGENT}

        response: Response = requests.get(url, params=params, headers=headers)

        return response
