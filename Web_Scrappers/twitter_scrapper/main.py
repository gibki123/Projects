from scrapper.twitter_scrapper import Scrapper
from configs.Elon_Musk_conf import ElonMusk
from configparser import ConfigParser

if __name__ == '__main__':
    config = ConfigParser()
    config.read('../app_config/config.ini')
    config.read('./twitter_config/login_conf.ini')
    config.read('./twitter_config/timing_conf.ini')
    scrapper = Scrapper(config, ElonMusk)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
