from .models import VechainCandle as VC
from .serializers import BulkVechainCandleSerializer
import requests
from decimal import Decimal
import logging
import json

COIN_CAP_API_BASE = 'https://api.coincap.io/v2'
CANDLE_API_BASE = COIN_CAP_API_BASE + '/candles?'

def make_candle_params(exchange: str, interval: str, base_id: str, quote_id: str) -> dict:
    ''' Make candle request's params

    Args:
        exchange (str): exchange name
        interval (str): data interval
        base_id  (str): base coin id
        quote_id (str): quote coin id
    
    Returns:
        params for requesting candle data
    '''
    return {
        'exchange': exchange,
        'interval': interval,
        'baseId':   base_id,
        'quoteId':  quote_id
    }

def collect_vechain_candle():
    ''' Collect VeChain candle data

    '''
    try:
        params = make_candle_params(VC.EXCHANGE, VC.INTERVAL, VC.BASE_ID, VC.QUOTE_ID)
        result = requests.get(CANDLE_API_BASE, params = params, timeout = 30)
        data = result.json().get('data', None)
        
        if data:
            for each in data:
                for key, value in each.items():
                    each[key] = float(value) if key != 'period' else int(value)
            
            serializer = BulkVechainCandleSerializer(data = data)
            
            if serializer.is_valid():
                serializer.save()
            else:
                logging.warning(str(serializer.errors))
        else:
            logging.info("No any VeChain Data")
    except Exception as e:
        logging.error(str(e))
    except requests.exceptions.Timeout:
        logging.error("Timeout")
