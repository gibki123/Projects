from dataclasses import dataclass, field
from typing import List, Dict
from selenium.webdriver.common.by import By
from Interfaces.config_interface import Element, PopupElement, ElementAttr


@dataclass(frozen=True)
class CoindeskBTC:
    url: str = field(default="https://www.coindesk.com/search?s=bitcoin&sort=1")
    name: str = field(default="CoindeskBTC")
    asset_name: str = field(default="BTC")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


########################################           ETH          #########################################################


@dataclass(frozen=True)
class CoindeskETH:
    url: str = field(default="https://www.coindesk.com/search?s=ethereum&sort=1")
    name: str = field(default="CoindeskETH")
    asset_name: str = field(default="ETH")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

    sleep_time_change_tab: float = field(default=1.0)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: ["https://www.coindesk.com/price/ethereum"])

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



########################################################################################################################
########################################           XRP          ########################################################
########################################################################################################################

@dataclass(frozen=True)
class CoindeskXRP:
    url: str = field(default="https://www.coindesk.com/search?s=xrp&sort=1")
    name: str = field(default="CoindeskXRP")
    asset_name: str = field(default="XRP")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

    sleep_time_change_tab: float = field(default=1.0)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: ["https://www.coindesk.com/price/xrp"])

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



@dataclass(frozen=True)
class CoindeskMARKETS:
    url: str = field(default="https://www.coindesk.com/search?s=markets&sort=1")
    name: str = field(default="CoindeskMARKETS")
    asset_name: str = field(default="MARKETS")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=True)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"



@dataclass(frozen=True)
class CoindeskREGULATION:
    url: str = field(default="https://www.coindesk.com/search?s=regulation&sort=1")
    name: str = field(default="CoindeskREGULATIONS")
    asset_name: str = field(default="REGUL")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=False)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


@dataclass(frozen=True)
class CoindeskPOLICY:
    url: str = field(default="https://www.coindesk.com/search?s=policy&sort=1")
    name: str = field(default="CoindeskPOLICY")
    asset_name: str = field(default="POLICY")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=False)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


@dataclass(frozen=True)
class CoindeskWEB3:
    url: str = field(default="https://www.coindesk.com/search?s=web3&sort=1")
    name: str = field(default="CoindeskWEB3")
    asset_name: str = field(default="WEB3")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=False)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"


@dataclass(frozen=True)
class CoindeskSTABLECOINS:
    url: str = field(default="https://www.coindesk.com/search?s=stablecoins&sort=1")
    name: str = field(default="CoindeskSTABLECOINS")
    asset_name: str = field(default="STABLE")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=False)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [
            PopupElement("CybotCookiebotDialogBodyButtonAccept", By.ID, 1),
        ]
    )

    type_of_list: str = field(default='STATIC')

    news_div_element: Element = field(default=Element(
        "searchstyles__ItemRow-ci5zlg-4", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("dYGcqp", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("at-category", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("at-headline", By.CLASS_NAME))

    subheadline_element: Element = field(  # no subheadline
        default=Element(name="at-subheadline", type=By.CLASS_NAME))

    authors_element: Element = field(
        default=Element(name="at-authors", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=ElementAttr(name="at-created", type=By.CLASS_NAME, attr='text'))

    update_date_and_time_element: Element = field(
        default=Element(name="at-updated", type=By.CLASS_NAME))

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

    months_dict: Dict[str, int] = field(default_factory=lambda: {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    })

    def parse_date_and_time(self, input_datetime: str) -> str:
        if (input_datetime is None):
            return "1900-01-01 00:00:00"
        else:
            # get rid of unnecessary words/characters
            input_datetime = input_datetime.replace(",", "")
            input_datetime = input_datetime.replace("Updated ", "")
            input_datetime = input_datetime.replace("at ", "")

            # split datetime into separate elements and format them properly
            month, day, year, hour_minute, am_pm = input_datetime.split(" ")
            month = self.months_dict[month]
            day = int(day)
            year = int(year)
            hour, minute = hour_minute.split(":")
            if am_pm == "p.m." and int(hour) != 12:
                hour = int(hour) + 12
            else:
                hour = int(hour)
            minute = int(minute)
            seconds = 0

            # return formatted fstring ready for db insertion
            return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{seconds:02d}"

