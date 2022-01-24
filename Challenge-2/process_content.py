import pandas as pd
import requests

BITCOIN_UUID = 'Qwsogvtv82FCd'
DEFAULT_TIME_PERIOD = '30d'


def fetch_coin_historical_data(coin_id: str = BITCOIN_UUID, timeframe: str = DEFAULT_TIME_PERIOD):
    """
        input: accepts timeframe as parameter
        fetch the bitcoin historical data from coinranking api for the given timeframe
        output: returns the historical data pandas dataframe
    """
    coin_history_api_url = f'https://api.coinranking.com/v2/coin/{}/history'
    coin_history_api_query_string_parameter = f'timePeriod={}'

    # TODO B: Make API Call

    return pd.read______("""Fill In""")


def get_coin_historical_data(old_df: pd.DataFrame):
    """
        Accepts coin_id and timeframe as input parameter (if not provided defaulted to bitcoin id (1) and timeframe 30 days)
        By default retrieves last 30days bitcoin historical data and
        parses the data into the JSON array contains the following schema JSON object
        Output schema:
        {
            "date": "{date}",
            "price": "{value}",
            "direction": "{up/down/same}",
            "change": "{amount}",
            "dayOfWeek": "{name}”,
            "highSinceStart": "{true/false}”,
            "lowSinceStart": "{true/false}”
        }
    """
    # TODO C: Transform API data into given schema and return JSON
    df = pd.DataFrame()
    df['change'] = old_df.price.shift(1) - old_df.price
    final_json = df._______("""Fill In""")
    return final_json


def handler():
    # TODO D: Call all methods in the handler code
    pass


# TODO A: Call appropriate main function
