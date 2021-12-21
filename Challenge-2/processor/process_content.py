# TODO : Do neccessary imports here

BITCOIN_HISTORY_API_URL = "https://api.coinranking.com/v1/public/coin/{}/history/{}"

def fetch_bitcoin_historical_data(coin_id, timeframe):
    '''
        input: accepts timeframe as parameter
        fetch the bitcoin historical data from coinranking api for the given timeframe
        output: returns the historical data pandas dataframe
    '''
    # TODO A: Read Bitcoin API


def get_bitcoin_historical_data(coin_id=1, timeframe='30d'):
    '''
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
    '''
    # TODO B: Transform API data into given schema and return JSON
    final_json = {}
    return final_json


def handler(event, context):
    '''
    :param event:
    :param context:
    :return:
    '''
    #TODO C: Call all methods in the handler code





