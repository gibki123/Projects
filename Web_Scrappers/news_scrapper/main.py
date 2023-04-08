from scrapper.news_scrapper import Scrapper
from configs.coindesk_conf import CoindeskBTC, CoindeskETH, CoindeskXRP, CoindeskMARKETS, CoindeskPOLICY,\
    CoindeskREGULATION, CoindeskWEB3, CoindeskSTABLECOINS
from configs.crypto_daily_conf import CryptoDailyBTC, CryptoDailyETH, CryptoDailyXRP, CryptoDailyBusiness,\
    CryptoDailyWeb3, CryptoDailyRegulation, CryptoDailySecurity
from configs.daily_coin_conf import DailyCoinBTC, DailyCoinETH, DailyCoinXRP, DailyCoinMarket, DailyCoinPolicy, \
    DailyCoinTech
from configs.cointelegraph_conf import CointelegraphBTC
from configs.reuters_conf import ReutersBusiness
from configs.euronews_conf import EuronewsEconomy, EuronewsBusiness, EuronewsMarkets

from configparser import ConfigParser
# 38

if __name__ == '__main__':
    parser = ConfigParser()
    parser.read('../app_config/config.ini')
    app_config = dict(parser.items('DEFAULT'))

    # website_config = CoindeskBTC()
    # website_config = CoindeskETH()
    # website_config = CoindeskXRP()
    # website_config = CoindeskMARKETS()
    # website_config = CoindeskPOLICY()
    # website_config = CoindeskREGULATION()
    # website_config = CoindeskWEB3()
    # website_config = CoindeskSTABLECOINS()

    # website_config = CointelegraphBTC()

    # website_config = CryptoDailyBTC()
    # website_config = CryptoDailyETH()
    # website_config = CryptoDailyXRP()
    # website_config = CryptoDailyBusiness()
    # website_config = CryptoDailyWeb3()
    # website_config = CryptoDailyRegulation()
    # website_config = CryptoDailySecurity()

    # website_config = DailyCoinBTC()
    # website_config = DailyCoinETH()
    # website_config = DailyCoinXRP()
    # website_config = DailyCoinMarket()
    # website_config = DailyCoinPolicy()
    # website_config = DailyCoinTech()

    # website_config = ReutersBusiness()

    website_config = EuronewsEconomy()
    # website_config = EuronewsMarkets()
    # website_config = EuronewsBusiness()


    db_config = ConfigParser()
    db_config.read('../database/db.ini')

    scrap_tool = Scrapper(app_config['driver_path'], db_config, website_config)
    scrap_tool.scrap_site()
