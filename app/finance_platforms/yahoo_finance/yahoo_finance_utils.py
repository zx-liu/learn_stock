import datetime
from typing import Any, Dict, List

from app.finance_platforms.yahoo_finance.yahoo_finance_constants import (
    YahooFinanceConstants,
)


class YahooFinanceUtils:
    """some helper functions used in Yahoo finance data retrieval"""

    @staticmethod
    def build_timeseries_api(
        base_endpoint: str, stock_code: str, timeseries_type: str, interval: str
    ) -> str:
        """

        Args:
            base_endpoint:
            stock_code:
            timeseries_type:
            interval:

        Returns:
            str: the target endpoint
        """
        timeseries: Dict[str, Any] = YahooFinanceConstants.ENDPOINT_TYPES["timeseries"]
        stats: List[str] = timeseries[timeseries_type]

        # 1. build query type in endpoint
        query_type: str = ",".join([interval + stat_name for stat_name in stats])

        # 2. build query start and end time in endpoint
        start_date: datetime.datetime = datetime.datetime(
            **YahooFinanceConstants.DEFAULT_QUERY_START_DATE, tzinfo=None
        )
        end_date: datetime.datetime = (
            datetime.datetime.now()
        )  # ignore timezones, should be fine

        # 3. concatenate them together
        url: str = (
            f"{base_endpoint}{stock_code}"
            f"?{YahooFinanceConstants.SYMBOL}={stock_code}"
            f"&{YahooFinanceConstants.TYPE}={query_type}"
            f"&{YahooFinanceConstants.PERIOD1}={int(start_date.timestamp())}"
            f"&{YahooFinanceConstants.PERIOD2}={int(end_date.timestamp())}"
        )

        return url
