from itertools import count

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from logging import getLogger

import logging

from time import sleep
from typing import List, Dict, Tuple, Optional, Union
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

from Interfaces.config_interface import Element
import psycopg2
from sys import exit

UPDATE_DATABASE = True

logging.basicConfig(filename="logs.log", format='%(asctime)s | %(levelname)s | %(message)s')

logger = getLogger(__name__)
logger.setLevel(logging.INFO)


class Scrapper:

    def __init__(self, driver_path, db_config, website_conf):
        self.website_conf = website_conf
        self.driver = Chrome(driver_path)
        self.db_config = db_config
        self._start_site()
        self.news_id = 0
        self.clicked_no_thanks = False

    def scrap_site(self, no_reloads: int = None) -> None:

        if self.website_conf.type_of_list == 'DYNAMIC':
            for _ in range(self.website_conf.load_articles_number):
                self._load_more_articles()

        if no_reloads is None:
            counter = count(start=1, step=1)
            while True:
                self._scrap_one_list()
                logger.info(f"Scrapped page {next(counter)}")
        else:
            for _ in range(no_reloads):
                self._scrap_one_list()

    def _start_site(self) -> None:
        self.driver.get(self.website_conf.url)
        self.driver.maximize_window()

        self._prepare_site()

    def _prepare_site(self) -> None:
        if self.website_conf.close_popups:
            self._close_all_popups()

        if hasattr(self.website_conf, 'login'):
            if self.website_conf.login:
                self.website_conf.login_func(self.driver)

    def _close_all_popups(self) -> None:
        for popup_el in self.website_conf.popup_element:
            self.driver.implicitly_wait(popup_el.time_waiting_s)
            button = self.driver.find_element(
                by=popup_el.type, value=popup_el.name)
            button.click()

    def _load_more_articles(self) -> None:
        load_articles_button = self.driver.find_element(
            by=self.website_conf.load_article_button.type, value=self.website_conf.load_article_button.name)
        load_articles_button.click()
        sleep(2)

    def _scrap_one_list(self) -> None:
        hrefs = self._get_news_list()

        scrapped_data = self._scrap_news_list(hrefs)
        if UPDATE_DATABASE:
            self._update_database(scrapped_data)
        else:
            logger.info(scrapped_data)
        self._click_next_news()

    def _get_news_list(self) -> List[str]:
        # TODO Change logic to be more Universal
        news_list = self.driver.find_elements(
            self.website_conf.news_div_element.type, value=self.website_conf.news_div_element.name)
        hrefs = []
        for i, news in enumerate(news_list):
            try:
                if news.tag_name == 'a':
                    hrefs.append(news.get_attribute('href'))
                else:
                    hrefs.append(news.find_element(
                        By.TAG_NAME, value='a').get_attribute('href'))
            except NoSuchElementException as e:
                logger.warning(f"Couldn't scrap data, no href: NoSuchElementException")
        self._remove_redundant_hrefs(hrefs)
        return hrefs

    def _remove_redundant_hrefs(self, hrefs) -> List[str]:
        for href in hrefs.copy():
            if href in self.website_conf.hrefs_to_ignore:
                hrefs.remove(href)
        return hrefs

    def _scrap_news_list(self, hrefs) -> List[Dict[str, str]]:
        # Open a new window
        self.driver.execute_script("window.open('');")

        # Switch to the new window and open new URLS
        self.driver.switch_to.window(self.driver.window_handles[1])

        full_list_data = []

        for href in hrefs:
            try:
                self.driver.get(href)
                if self.website_conf.name == 'EuroNews':
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                #     self.clicked_no_thanks = self.website_conf.find_click_not_thanks_popup(self.driver)
                paragraphs, headers = self._get_content_news_info()
                general_info = self._get_general_news_info()
                general_info = self._check_nulls(general_info)

                sleep(self.website_conf.sleep_time_change_tab)

                single_entry_data = general_info

                single_entry_data['news_text'] = '\n'.join(paragraphs)
                single_entry_data['news_text'] = single_entry_data['news_text'].strip()
                if headers:
                    single_entry_data['news_topics'] = '\n'.join(headers)
                else:
                    single_entry_data['news_topics'] = ''
                single_entry_data['source_url'] = href

                full_list_data.append(single_entry_data)
            except AttributeError as e:
                logger.warning(f"Couldn't scrap data from {href}: AttributeError")
                print(e)
            except NoSuchElementException as e:
                logger.warning(f"Couldn't scrap data from {href}: NoSuchElementException")
                print(e)
            except TimeoutException as e:
                logger.warning(f"Couldn't scrap data from {href}: TimeoutException")
                print(e)
            except StaleElementReferenceException as e:
                logger.warning(f"Couldn't scrap data from {href}: StaleElementReferenceException")
                print(e)

        # Closing new_url tab
        self.driver.close()

        # Switching to old tab
        self.driver.switch_to.window(self.driver.window_handles[0])

        return full_list_data

    def _limit_news_text(self, text):
        max_chars = self.website_conf.max_news_text_len - len("...")
        # truncate after the last word (to avoid middle word truncation)
        text = text[:text[:max_chars].rfind(' ')]
        # add trailing dots
        text += "..."

        return text

    def _truncate_text(self, text, max_chars):
        return text[:max_chars] if len(text) > max_chars else text

    def _get_content_news_info(self) -> Tuple[List[str], List[str]]:
        paragraphs = self._get_elements(
            'p', self.website_conf.cut_last_news_paragraphs)
        try:
            headers = self._get_elements(
                'h2', self.website_conf.cut_last_news_headers)
        except TimeoutException:
            logger.warning(f"Didnt scrap headers")
            headers = []
        return paragraphs, headers

    def _get_elements(self, tag_name: str, no_elements_to_cut: int) -> List[str]:
        self.driver.implicitly_wait(3)
        news_content = self._get_optional_element(
            finder=self.driver, elem_to_find=self.website_conf.news_content_element)
        WebDriverWait(self.driver, timeout=1).until(lambda d: d.find_elements(by=By.TAG_NAME, value=tag_name))
        elements = news_content.find_elements(
            by=By.TAG_NAME, value=tag_name)
        elements = [p.text.strip() for p in elements]
        if no_elements_to_cut > 0:
            elements = elements[:-no_elements_to_cut]
        return elements

    def _get_general_news_info(self) -> Dict[str, str]:
        article_general = self._get_optional_element(
            finder=self.driver, elem_to_find=self.website_conf.article_general_element)

        category = self._get_optional_element_attr(
            finder=article_general, elem_to_find=self.website_conf.category_element, attr='text')

        headline = self._get_optional_element_attr(
            finder=article_general, elem_to_find=self.website_conf.headline_element, attr='text')

        subheadline = self._get_optional_element_attr(
            finder=article_general, elem_to_find=self.website_conf.subheadline_element, attr='text')

        authors = self._get_optional_element_attr(
            finder=article_general, elem_to_find=self.website_conf.authors_element, attr='text')
        authors = self.website_conf.parse_authors(authors=authors)

        date_and_time = self._get_optional_element_attr(
            finder=article_general,
            elem_to_find=self.website_conf.create_date_and_time_element,
            attr='text')

        if (date_and_time is None) | (date_and_time == ""):
            date_and_time = self._get_optional_element_attr(
                finder=article_general, elem_to_find=self.website_conf.update_date_and_time_element, attr='text')
        date_and_time = self.website_conf.parse_date_and_time(
            input_datetime=date_and_time)

        no_comments = self._get_optional_element_attr(
            finder=article_general, elem_to_find=self.website_conf.no_comments_element, attr='text')
        no_views = self._get_optional_element_attr(
            finder=article_general, elem_to_find=self.website_conf.no_views_element, attr='text')

        self.news_id += 1

        return {
            'asset_name': self.website_conf.asset_name,
            'category': category if category is not None else "-",
            'headline': headline,
            'subheadline': subheadline if subheadline is not None else "-",
            'authors': authors,
            'date_and_time': date_and_time,
            'is_by_relevance': self.website_conf.is_by_relevance,
            'id_per_news': self.news_id,
            'source_name': self.website_conf.name,
            'no_comments': no_comments if no_comments is not None else 0,
            'no_views': no_views if no_views is not None else 0
        }

    def _check_nulls(self, data_dict: Dict) -> Dict:
        str_cols = ['category', 'headline', 'subheadline', 'authors', 'date_and_time', 'source_name']
        int_cols = ['is_by_relevance', 'id_per_news', 'no_comments', 'no_views']

        for key, value in data_dict.items():
            if (value is None) or (value == ""):
                if key in str_cols:
                    data_dict[key] = '-'
                elif key in int_cols:
                    data_dict[key] = 0
                else:
                    logger.error(f"Key not found in possible columns during null validation")
                logger.warning(f"Key {key} was NULL")

        return data_dict

    def _get_optional_element(self, finder: Union[Chrome, WebElement], elem_to_find: Element) -> Optional[WebElement]:
        if len(elem_to_find.name) == 0:
            return None

        try:
            found_elem = finder.find_element(
                by=elem_to_find.type, value=elem_to_find.name)
            return found_elem
        except NoSuchElementException:
            return None

    def _get_optional_element_attr(self, finder: Union[Chrome, WebElement], elem_to_find: Element, attr: str) -> \
            Optional[str]:
        try:
            opt_elem = self._get_optional_element(
                finder=finder, elem_to_find=elem_to_find)
            return getattr(opt_elem, attr)
        except AttributeError:
            return None

    def _click_next_news(self) -> None:
        self.driver.implicitly_wait(1)
        next_news_button = self.driver.find_element(
            self.website_conf.next_news_btn.type, value=self.website_conf.next_news_btn.name)

        action = ActionChains(self.driver)

        action.scroll_by_amount(
            delta_x=0, delta_y=next_news_button.location['y'] - 340).perform()
        sleep(1)
        next_news_button.click()
        self.driver.implicitly_wait(2)

    def _update_database(self, scrapped_data) -> None:
        try:
            conn = None
            conn = psycopg2.connect(
                database=self.db_config['postgresql']['db'],
                user=self.db_config['postgresql']['user'],
                password=self.db_config['postgresql']['passwd'],
                host=self.db_config['postgresql']['host'],
                port=self.db_config['postgresql']['port'],
                connect_timeout=self.db_config['postgresql'].getint(
                    'conn_timeout')
            )
            cursor = conn.cursor()

            for data in scrapped_data:
                cursor.execute(""" INSERT INTO news_data_table (asset_name, headline, news_text, authors, 
                                source_url, source_name, date_and_time, per_source_id,
                                is_by_relavance, category, subheadline, no_comments, no_views)
                                VALUES(%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                               (data['asset_name'], data['headline'], data['news_text'], data['authors'],
                                data['source_url'], data['source_name'], data['date_and_time'],
                                data['id_per_news'], data['is_by_relevance'], data['category'],
                                data['subheadline'], data['no_comments'], data['no_views']))

            conn.commit()

        except psycopg2.DatabaseError as e:
            print(f"Database error {e}")
            # TODO: how should it be handled
            exit(1)

        finally:
            if conn:
                conn.close()