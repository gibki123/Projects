from selenium import webdriver
from selenium.webdriver import Keys
from configparser import ConfigParser
from bs4 import BeautifulSoup
from unicodedata import normalize

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

# TODO: Better function structuring


class Scrapper:

    def __init__(self, config, website_conf):
        self.tweets_data = []

        self.website_conf = website_conf()
        self.timing_conf = config['timing']
        self.login_info = config['keys']
        self.driver = webdriver.Chrome(config['DEFAULT']['driver_path'])
        self._start_site(self.website_conf.url)
        self._prepare_site()
        self._get_full_data()

    def _start_site(self, url: str) -> None:
        self.driver.get(url)
        self.driver.maximize_window()

    def _prepare_site(self) -> None:
        self.driver.implicitly_wait(self.timing_conf.getint('implicit_wait'))
        if self.website_conf.close_popups:
            self._close_all_popups()

        self._login()
        sleep(1)
        self.driver.get(self.website_conf.url)

    def _close_all_popups(self) -> None:
        for time, value, search_type in zip(self.website_conf.times_popup_waiting, self.website_conf.popup_names,
                                            self.website_conf.popup_types):
            sleep(time)
            button = self.driver.find_element(by=search_type, value=value)
            button.click()

    def _login(self) -> None:
        self.driver.implicitly_wait(self.timing_conf.getint('implicit_wait'))
        self.driver.find_element(
            by=By.XPATH, value=self.website_conf.login_button).click()

        self.driver.implicitly_wait(self.timing_conf.getint('implicit_wait'))
        self.driver.find_element(by=By.XPATH, value=self.website_conf.mail_input).send_keys(
            self.login_info['email'])
        self.driver.implicitly_wait(self.timing_conf.getint('implicit_wait'))
        self.driver.find_element(
            by=By.XPATH, value=self.website_conf.next_login_button).click()

        logged = False
        while not logged:
            try:
                self.driver.implicitly_wait(
                    self.timing_conf.getint('implicit_wait'))
                self.driver.find_element(by=By.XPATH, value=self.website_conf.password_input).send_keys(
                    self.login_info['password'])
                self.driver.implicitly_wait(
                    self.timing_conf.getint('implicit_wait'))
                self.driver.find_element(
                    by=By.XPATH, value=self.website_conf.final_login_button).click()
                logged = True
            except:
                self.driver.implicitly_wait(
                    self.timing_conf.getint('implicit_wait'))
                self.driver.find_element(by=By.XPATH, value=self.website_conf.phone_input).send_keys(
                    self.login_info['phone_number'])
                self.driver.implicitly_wait(
                    self.timing_conf.getint('implicit_wait'))
                self.driver.find_element(
                    by=By.XPATH, value=self.website_conf.next_phone_button).click()
        # TODO: handle 2-step verification. Twitter might ask for additional verification code when account have it enabled

    def _load_articles_selenium(self):

        articles = self.driver.find_elements(By.TAG_NAME, "article")
        return articles

    def _load_articles(self):

        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        articles = soup.find_all('article')

        return articles

    def _get_last_old_index(self, tweet_dicts) -> int:
        if len(self.tweets_data) > 0:
            for i, dict in enumerate(tweet_dicts, 0):
                if dict == self.tweets_data[-1]:
                    return i
            return -1
        else:
            return -1

    def _get_tweets_data(self, articles) -> None:
        tweet_dicts = []
        for i, article in enumerate(articles):

            spans = article.find_all('span')
            ases = article.find_all('a')
            prepared_dict = self._get_correct_data_dict(spans, ases)
            print(i)
            for span in spans:
                print(span.text)
            for a in ases:
                print(a.text)
            tweet_dicts.append(prepared_dict)

        first_new_tweet_index = self._get_last_old_index(tweet_dicts) + 1
        self.tweets_data.extend(tweet_dicts[first_new_tweet_index:])

    def _get_correct_data_dict(self, spans, ases):
        tweet_dict = {}
        if 'podał/a dalej Tweeta' in spans[0].text:
            tweet_dict['author'] = spans[1].text
            tweet_dict['second_author'] = spans[3].text
            tweet_dict['retweet_flg'] = 1
            tweet_dict['content'] = spans[7].text
            tweet_dict['comments'] = spans[-9].text.replace('\xa0', '')
            tweet_dict['retweets'] = spans[-6].text.strip().replace('\xa0', '')
            tweet_dict['likes'] = spans[-3].text.strip().replace('\xa0', '')

        elif 'Cytuj Tweeta' in spans[5].text:
            tweet_dict['author'] = spans[0].text
            tweet_dict['second_author'] = spans[6].text
            tweet_dict['retweet_flg'] = 0
            tweet_dict['content'] = spans[4].text
            tweet_dict['comments'] = spans[-7].text.strip().replace('\xa0', '')
            tweet_dict['retweets'] = spans[-4].text.strip().replace('\xa0', '')
            tweet_dict['likes'] = spans[-1].text.strip().replace('\xa0', '')

        else:
            tweet_dict['author'] = spans[0].text
            tweet_dict['second_author'] = ''
            tweet_dict['retweet_flg'] = 0
            tweet_dict['content'] = spans[4].text
            tweet_dict['comments'] = spans[5].text.strip().replace('\xa0', '')
            tweet_dict['retweets'] = spans[8].text.strip().replace('\xa0', '')
            tweet_dict['likes'] = spans[11].text.strip().replace('\xa0', '')

        if (ases[-1].text is not None) and (ases[-1].text != "") and (len(ases[-1].text) <= 15):
            tweet_dict['time'] = ases[-1].text
        elif (ases[-2].text is not None) and (ases[-2].text != "") and (len(ases[-2].text) <= 15):
            tweet_dict['time'] = ases[-2].text
        else:
            tweet_dict['time'] = ases[-3].text

        return tweet_dict

    def _get_full_data(self) -> None:
        self.driver.implicitly_wait(self.timing_conf.getint('implicit_wait'))
        # Get scroll height
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            sleep(3)
            articles_selenium = self._load_articles_selenium()
            articles = self._load_articles()
            self._get_tweets_data(articles)

            # Scroll down to bottom
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", articles_selenium[-1])

            # Wait to load page
            sleep(self.timing_conf.getfloat('scroll_pause'))

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
