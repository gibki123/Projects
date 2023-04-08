from dataclasses import dataclass, field
from typing import List
from selenium.webdriver.common.by import By
from Interfaces.config_interface import Element, PopupElement, ElementAttr
import datetime


@dataclass(frozen=True)
class CryptoDailyBTC:
    url: str = field(default="https://cryptodaily.co.uk/search?q=bitcoin")
    name: str = field(default="CryptoDaily")
    asset_name: str = field(default="BTC")

    close_popups: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("(//button[@class=' css-13h9oak'])[1]", By.XPATH, 2),
        ]
    )

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(
        default=Element("post-item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("news-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(  # TODO
        "//a[contains(text(),'›')]", By.XPATH))

    category_element: Element = field(
        default=Element("post-main-tag", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post-title", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="", type=By.XPATH))

    authors_element: Element = field(
        default=Element(name="post_author_name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="date-count", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.0)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: ["https://www.coindesk.com/price/bitcoin"])

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
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[-3:]
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
class CryptoDailyETH:
    url: str = field(default="https://cryptodaily.co.uk/search?q=ethereum")
    name: str = field(default="CryptoDaily")
    asset_name: str = field(default="ETH")

    close_popups: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("(//button[@class=' css-13h9oak'])[1]", By.XPATH, 2),
        ]
    )

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(
        default=Element("post-item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("news-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(  # TODO
        "//a[contains(text(),'›')]", By.XPATH))

    category_element: Element = field(
        default=Element("post-main-tag", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post-title", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="", type=By.XPATH))

    authors_element: Element = field(
        default=Element(name="post_author_name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="date-count", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.0)

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
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[-3:]
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
class CryptoDailyXRP:
    url: str = field(default="https://cryptodaily.co.uk/search?q=xrp")
    name: str = field(default="CryptoDaily")
    asset_name: str = field(default="XRP")

    close_popups: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("(//button[@class=' css-13h9oak'])[1]", By.XPATH, 2),
        ]
    )

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(
        default=Element("post-item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("news-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(  # TODO
        "//a[contains(text(),'›')]", By.XPATH))

    category_element: Element = field(
        default=Element("post-main-tag", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post-title", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="", type=By.XPATH))

    authors_element: Element = field(
        default=Element(name="post_author_name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="date-count", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.0)

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
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[-3:]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


########################################################################################################################
########################################           BUSINESS          ########################################################
########################################################################################################################

@dataclass(frozen=True)
class CryptoDailyBusiness:
    url: str = field(default="https://cryptodaily.co.uk/search?q=business")
    name: str = field(default="CryptoDaily")
    asset_name: str = field(default="BUSINESS")

    close_popups: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("(//button[@class=' css-13h9oak'])[1]", By.XPATH, 2),
        ]
    )

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(
        default=Element("post-item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("news-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(  # TODO
        "//a[contains(text(),'›')]", By.XPATH))

    category_element: Element = field(
        default=Element("post-main-tag", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post-title", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="", type=By.XPATH))

    authors_element: Element = field(
        default=Element(name="post_author_name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="date-count", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.0)

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
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[-3:]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



########################################################################################################################
########################################           WEB3          ########################################################
########################################################################################################################

@dataclass(frozen=True)
class CryptoDailyWeb3:
    url: str = field(default="https://cryptodaily.co.uk/search?q=WEB3")
    name: str = field(default="CryptoDaily")
    asset_name: str = field(default="WEB3")

    close_popups: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("(//button[@class=' css-13h9oak'])[1]", By.XPATH, 2),
        ]
    )

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(
        default=Element("post-item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("news-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(  # TODO
        "//a[contains(text(),'›')]", By.XPATH))

    category_element: Element = field(
        default=Element("post-main-tag", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post-title", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="", type=By.XPATH))

    authors_element: Element = field(
        default=Element(name="post_author_name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="date-count", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.0)

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
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[-3:]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



########################################################################################################################
########################################           REGULATION          ########################################################
########################################################################################################################

@dataclass(frozen=True)
class CryptoDailyRegulation:
    url: str = field(default="https://cryptodaily.co.uk/search?q=regulation")
    name: str = field(default="CryptoDaily")
    asset_name: str = field(default="REGULATION")

    close_popups: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("(//button[@class=' css-13h9oak'])[1]", By.XPATH, 2),
        ]
    )

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(
        default=Element("post-item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("news-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(  # TODO
        "//a[contains(text(),'›')]", By.XPATH))

    category_element: Element = field(
        default=Element("post-main-tag", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post-title", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="", type=By.XPATH))

    authors_element: Element = field(
        default=Element(name="post_author_name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="date-count", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.0)

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
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[-3:]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



########################################################################################################################
########################################           SECIRITY          ########################################################
########################################################################################################################

@dataclass(frozen=True)
class CryptoDailySecurity:
    url: str = field(default="https://cryptodaily.co.uk/search?q=security")
    name: str = field(default="CryptoDaily")
    asset_name: str = field(default="SECURITY")

    close_popups: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("(//button[@class=' css-13h9oak'])[1]", By.XPATH, 2),
        ]
    )

    is_by_relevance: bool = field(default=False)

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(
        default=Element("post-item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("body", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("news-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(  # TODO
        "//a[contains(text(),'›')]", By.XPATH))

    category_element: Element = field(
        default=Element("post-main-tag", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post-title", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="", type=By.XPATH))

    authors_element: Element = field(
        default=Element(name="post_author_name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="date-count", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=create_date_and_time_element)  # same as created

    sleep_time_change_tab: float = field(default=1.0)

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
            input_datetime = input_datetime.strip()
            input_datetime = input_datetime.replace("  ", " ")

            month, day, year = input_datetime.split(" ")[-3:]
            month = datetime.datetime.strptime(month, "%B").month
            day = int(day)
            year = int(year)
            hour = 0
            minute = 0
            seconds = 0
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"

