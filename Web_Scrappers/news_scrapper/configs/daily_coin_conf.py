from dataclasses import dataclass, field
from typing import List
from selenium.webdriver.common.by import By
from Interfaces.config_interface import Element, PopupElement, ElementAttr
import datetime


@dataclass(frozen=True)
class DailyCoinBTC:
    url: str = field(default="https://dailycoin.com/?s=bitcoin")
    name: str = field(default="DailyCoin")
    asset_name: str = field(default="BTC")

    close_popups: bool = field(default=False)

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("//button[@id='CybotCookiebotDialogBodyLevelButtonAccept']", By.XPATH, 10)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("mkd-post-text", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//span[@class='mkd-pagination-icon arrow_carrot-right']", By.XPATH))

    category_element: Element = field(
        default=Element("", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("h1", By.TAG_NAME))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="mkd-post-info-author", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="mkd-post-info-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    max_news_text_len: int = field(default=700)

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
        if (input_datetime is None):
            return ""
        else:
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[:3]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"

########################################################################################################################
########################################           ETH          ########################################################
########################################################################################################################

@dataclass(frozen=True)
class DailyCoinETH:
    url: str = field(default="https://dailycoin.com/?s=ethereum")
    name: str = field(default="DailyCoin")
    asset_name: str = field(default="ETH")

    close_popups: bool = field(default=False)

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("//button[@id='CybotCookiebotDialogBodyLevelButtonAccept']", By.XPATH, 10)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("mkd-post-text", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//span[@class='mkd-pagination-icon arrow_carrot-right']", By.XPATH))

    category_element: Element = field(
        default=Element("", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("h1", By.TAG_NAME))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="mkd-post-info-author", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="mkd-post-info-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    max_news_text_len: int = field(default=700)

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
        if (input_datetime is None):
            return ""
        else:
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[:3]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


########################################################################################################################
########################################           XRP          ########################################################
########################################################################################################################


@dataclass(frozen=True)
class DailyCoinXRP:
    url: str = field(default="https://dailycoin.com/?s=xrp")
    name: str = field(default="DailyCoin")
    asset_name: str = field(default="XRP")

    close_popups: bool = field(default=False)

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("//button[@id='CybotCookiebotDialogBodyLevelButtonAccept']", By.XPATH, 10)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("mkd-post-text", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//span[@class='mkd-pagination-icon arrow_carrot-right']", By.XPATH))

    category_element: Element = field(
        default=Element("", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("h1", By.TAG_NAME))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="mkd-post-info-author", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="mkd-post-info-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    max_news_text_len: int = field(default=700)

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
        if (input_datetime is None):
            return ""
        else:
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[:3]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



########################################################################################################################
########################################           MARKET       ########################################################
########################################################################################################################


@dataclass(frozen=True)
class DailyCoinMarket:
    url: str = field(default="https://dailycoin.com/?s=market")
    name: str = field(default="DailyCoin")
    asset_name: str = field(default="MARKET")

    close_popups: bool = field(default=False)

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("//button[@id='CybotCookiebotDialogBodyLevelButtonAccept']", By.XPATH, 10)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("mkd-post-text", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//span[@class='mkd-pagination-icon arrow_carrot-right']", By.XPATH))

    category_element: Element = field(
        default=Element("", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("h1", By.TAG_NAME))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="mkd-post-info-author", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="mkd-post-info-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    max_news_text_len: int = field(default=700)

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
        if (input_datetime is None):
            return ""
        else:
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[:3]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


########################################################################################################################
########################################           POLICY       ########################################################
########################################################################################################################


@dataclass(frozen=True)
class DailyCoinPolicy:
    url: str = field(default="https://dailycoin.com/?s=policy")
    name: str = field(default="DailyCoin")
    asset_name: str = field(default="POLICY")

    close_popups: bool = field(default=False)

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("//button[@id='CybotCookiebotDialogBodyLevelButtonAccept']", By.XPATH, 10)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("mkd-post-text", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//span[@class='mkd-pagination-icon arrow_carrot-right']", By.XPATH))

    category_element: Element = field(
        default=Element("", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("h1", By.TAG_NAME))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="mkd-post-info-author", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="mkd-post-info-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    max_news_text_len: int = field(default=700)

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
        if (input_datetime is None):
            return ""
        else:
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[:3]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



########################################################################################################################
########################################           TECH       ########################################################
########################################################################################################################


@dataclass(frozen=True)
class DailyCoinTech:
    url: str = field(default="https://dailycoin.com/?s=tech")
    name: str = field(default="DailyCoin")
    asset_name: str = field(default="TECH")

    close_popups: bool = field(default=False)

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("//button[@id='CybotCookiebotDialogBodyLevelButtonAccept']", By.XPATH, 10)])

    news_div_element: Element = field(
        default=Element("article", By.TAG_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("mkd-post-text", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//span[@class='mkd-pagination-icon arrow_carrot-right']", By.XPATH))

    category_element: Element = field(
        default=Element("", By.XPATH))  # no category

    headline_element: Element = field(
        default=Element("h1", By.TAG_NAME))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="mkd-post-info-author", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="mkd-post-info-date", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    max_news_text_len: int = field(default=700)

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
        if (input_datetime is None):
            return ""
        else:
            # get rid of non standard ascii characters
            input_datetime = input_datetime.encode("ascii", "ignore").decode()

            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("|", "")
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[:3]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"
