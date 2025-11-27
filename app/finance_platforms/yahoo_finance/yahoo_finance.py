from typing import Any, Dict

from app.finance_platforms.yahoo_finance.yahoo_finance_constants import (
    YahooFinanceConstants,
)
from app.finance_platforms.yahoo_finance.yahoo_finance_utils import YahooFinanceUtils
from app.utils.request_utils import RequestUtil


class YahooFinance:
    """functions to retrieve financial data from Yahoo finance"""

    @staticmethod
    def get_balance_sheet(stock_code: str) -> Dict[str, Any]:
        """

        Args:
            stock_code:

        Returns:
            Dict[str, Any]:
        """
        url: str = YahooFinanceUtils.build_timeseries_api(
            base_endpoint=YahooFinanceConstants.BASE_ENDPOINTS["timeseries"],
            stock_code=stock_code,
            timeseries_type="balance-sheet",
            interval="annual",
        )

        response = RequestUtil.get_request(url)

        return response.json()
