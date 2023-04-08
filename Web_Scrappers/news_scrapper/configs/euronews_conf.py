from dataclasses import dataclass, field
from typing import List
from selenium.webdriver.common.by import By
from Interfaces.config_interface import Element, PopupElement, ElementAttr
import datetime
from selenium.webdriver import Chrome
from time import sleep


@dataclass(frozen=True)
class EuronewsEconomy:
    url: str = field(default="https://www.euronews.com/search?query=economy&p=152")
    name: str = field(default="EuroNews")
    asset_name: str = field(default="Economy")

    is_by_relevance: bool = field(default=False)

    close_popups: bool = field(default=True)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("(//button[@aria-label='Agree and close: Agree to our data processing and close'])[1]", By.XPATH, 2)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("//div[@id='poool-content']", By.XPATH))

    next_news_btn: Element = field(default=Element(
        "(//a[@class='c-paginator__text c-next'])[1]", By.XPATH))

    category_element: Element = field(
        default=Element("(//div[contains(@class,'c-article-labels')])[2]", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("(//h1[@class='c-article-title'])[2]", By.XPATH))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="(//div[contains(@class,'c-article-contributors')])[2]", type=By.XPATH))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="c-article-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=ElementAttr(name="(//time[contains(@class,'c-article-date')])[2]", type=By.XPATH, attr='text'))  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    # views aren't displyed on coindesk
    no_views_element: Element = field(
        default=Element(name="", type=By.XPATH))

    # there are no comments on coindesk
    no_comments_element: Element = field(
        default=Element(name="", type=By.XPATH))

    def parse_authors(self, authors: str) -> List[str]:
        if (authors is None):
            return []  # empty
        else:
            authors = authors.replace('By ', '')
            authors = authors.strip()
            authors = authors.split(',')
            return [a.strip() for a in authors]

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None) | (input_datetime == ""):
            return ""
        else:
            print(input_datetime)
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("/", " ")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            print(input_datetime.split(" "))

            day, month, year = input_datetime.split(" ")[1:4]
            month = int(month)
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


    def find_click_not_thanks_popup(self, driver: Chrome):
        driver.implicitly_wait(5)
        try:
            span = driver.find_element(By.CLASS_NAME, "p3-subactions")
            if span:
                span.click()
                return True
        except:
            print('no thanks not found')
            print(driver.page_source)

        return False



@dataclass(frozen=True)
class EuronewsMarkets:
    url: str = field(default="https://www.euronews.com/search?query=markets&p=255")
    name: str = field(default="EuroNews")
    asset_name: str = field(default="Markets")

    is_by_relevance: bool = field(default=False)

    close_popups: bool = field(default=True)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("(//button[@aria-label='Agree and close: Agree to our data processing and close'])[1]", By.XPATH, 2)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("//div[@id='poool-content']", By.XPATH))

    next_news_btn: Element = field(default=Element(
        "(//a[@class='c-paginator__text c-next'])[1]", By.XPATH))

    category_element: Element = field(
        default=Element("(//div[contains(@class,'c-article-labels')])[2]", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("(//h1[@class='c-article-title'])[2]", By.XPATH))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="(//div[contains(@class,'c-article-contributors')])[2]", type=By.XPATH))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="c-article-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=ElementAttr(name="(//time[contains(@class,'c-article-date')])[2]", type=By.XPATH, attr='text'))  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    # views aren't displyed on coindesk
    no_views_element: Element = field(
        default=Element(name="", type=By.XPATH))

    # there are no comments on coindesk
    no_comments_element: Element = field(
        default=Element(name="", type=By.XPATH))

    def parse_authors(self, authors: str) -> List[str]:
        if (authors is None):
            return []  # empty
        else:
            authors = authors.replace('By ', '')
            authors = authors.strip()
            authors = authors.split(',')
            return [a.strip() for a in authors]

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None) | (input_datetime == ""):
            return ""
        else:
            print(input_datetime)
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("/", " ")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            print(input_datetime.split(" "))

            day, month, year = input_datetime.split(" ")[1:4]
            month = int(month)
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


    def find_click_not_thanks_popup(self, driver: Chrome):
        driver.implicitly_wait(5)
        try:
            span = driver.find_element(By.CLASS_NAME, "p3-subactions")
            if span:
                span.click()
                return True
        except:
            print('no thanks not found')
            print(driver.page_source)

        return False




@dataclass(frozen=True)
class EuronewsBusiness:
    url: str = field(default="https://www.euronews.com/search?query=business&p=407")
    name: str = field(default="EuroNews")
    asset_name: str = field(default="Business")

    is_by_relevance: bool = field(default=False)

    close_popups: bool = field(default=True)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("(//button[@aria-label='Agree and close: Agree to our data processing and close'])[1]", By.XPATH, 2)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("//div[@id='poool-content']", By.XPATH))

    next_news_btn: Element = field(default=Element(
        "(//a[@class='c-paginator__text c-next'])[1]", By.XPATH))

    category_element: Element = field(
        default=Element("(//div[contains(@class,'c-article-labels')])[2]", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("(//h1[@class='c-article-title'])[2]", By.XPATH))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="(//div[contains(@class,'c-article-contributors')])[2]", type=By.XPATH))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="c-article-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=ElementAttr(name="(//time[contains(@class,'c-article-date')])[2]", type=By.XPATH, attr='text'))  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    # views aren't displyed on coindesk
    no_views_element: Element = field(
        default=Element(name="", type=By.XPATH))

    # there are no comments on coindesk
    no_comments_element: Element = field(
        default=Element(name="", type=By.XPATH))

    def parse_authors(self, authors: str) -> List[str]:
        if (authors is None):
            return []  # empty
        else:
            authors = authors.replace('By ', '')
            authors = authors.strip()
            authors = authors.split(',')
            return [a.strip() for a in authors]

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None) | (input_datetime == ""):
            return ""
        else:
            print(input_datetime)
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("/", " ")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            print(input_datetime.split(" "))

            day, month, year = input_datetime.split(" ")[1:4]
            month = int(month)
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


    def find_click_not_thanks_popup(self, driver: Chrome):
        driver.implicitly_wait(5)
        try:
            span = driver.find_element(By.CLASS_NAME, "p3-subactions")
            if span:
                span.click()
                return True
        except:
            print('no thanks not found')
            print(driver.page_source)

        return False
