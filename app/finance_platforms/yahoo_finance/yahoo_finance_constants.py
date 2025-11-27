from typing import Dict, List


class YahooFinanceConstants:
    """
    Rule 1: all endpoint constants must end with `/` for consistency.
    """

    # =============== End point related ===============
    # Q: Where do we get these endpoints?
    # A: Unfortunately I didn't find any documentation, pretty much all of them are from an open source repo
    #    https://github.com/ranaroussi/yfinance

    ENDPOINT_TYPES = {
        "timeseries": {
            "balance-sheet": [
                "TotalAssets",
                "TotalLiabilitiesNetMinorityInterest",
                "TotalEquityGrossMinorityInterest",
            ],
            "financials": [],
            "cash-flow": [],
        }
    }

    BASE_ENDPOINTS: Dict[str, str] = {
        "timeseries": "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"
    }

    SYMBOL: str = "symbol"

    ANNUAL: str = "annual"
    QUARTERLY: str = "quarterly"
    INTERVALS: List[str] = [ANNUAL, QUARTERLY]

    TYPE: str = "type"
    PERIOD1: str = "period1"
    PERIOD2: str = "period2"
    QUERY_PARAMETERS: List[str] = [TYPE, PERIOD1, PERIOD2]

    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

    # 2016/01/01, safe to act as most of the starting time on queries
    DEFAULT_QUERY_START_DATE: Dict[str, int] = {"year": 2016, "month": 1, "day": 1}

    # =============== Stock name related  ===============
