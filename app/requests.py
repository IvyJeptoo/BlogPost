import requests
from .models import Quote

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    '''
    consume request and return quote class instance
    '''
    response = requests.get(url).json()
    
    random_quote = Quote(response.get('author'),response.get('quote'))
    return random_quote