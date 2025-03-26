from settings import TOKEN_API, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from src.api.api_client import APIClient
from src.database.database_operations import insert_into_database
from src.database.settings_database import DatabaseConnection
from src.utils.generate_params import GenerateParams

if __name__ == '__main__':

    range_search = '5d'
    interval = '1d'
    fundamental = 'false'
    dividend = 'false'
    modules = 'summaryProfile'
    columns = ['currency', 'market_cap', 'short_name', 'long_name',
               'regular_market_change', 'regular_market_change_percent', 'regular_market_time', 'regular_market_price',
               'regular_market_day_high', 'regular_market_day_range', 'regular_market_day_low',
               'regular_market_volume', 'regular_market_previous_close', 'regular_market_open', 'fifty_two_week_range',
               'fifty_two_week_low', 'fifty_two_week_high', 'symbol', 'summary_profile', 'price_earnings',
               'earnings_per_share', 'logo_url']
    conn = DatabaseConnection(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    conn = conn.get_connection()
    acoes = ['LMTB34', 'NOCG34']
    for acoe in acoes:
        print(acoe)
        url_api = f"https://brapi.dev/api/quote/{acoe}"
        generate_parans = GenerateParams(acoe, range_search, interval, fundamental, dividend, modules, TOKEN_API)
        params = generate_parans.get_params()
        print(params)
        api_request = APIClient(url_api, params)
        result = api_request.request()['results'][0]
        insert_into_database(conn, table='raw_quote', columns=columns, data=result)
