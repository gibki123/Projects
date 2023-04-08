from dataclasses import dataclass, field
from typing import List, Dict
from selenium.webdriver.common.by import By
from Interfaces.config_interface import Element, PopupElement, ElementAttr
from datetime import datetime


@dataclass(frozen=True)
class CointelegraphBTC:
    url: str = field(default="https://cointelegraph.com/tags/bitcoin")
    name: str = field(default="CointelegraphBTC")
    asset_name: str = field(default="BTC")

    close_popups: bool = field(default=True)

    is_by_relevance: bool = field(default=False)

    popup_element: List[PopupElement] = field(
        default_factory=lambda: [PopupElement("//button[@class='btn privacy-policy__accept-btn']", By.XPATH, 1),
                                 ]
    )

    type_of_list: str = field(default='DYNAMIC')
    load_articles_number: int = field(default=5)

    load_article_button: Element = field(default=Element(
        "posts-listing__more-btn", By.CLASS_NAME))

    news_div_element: Element = field(default=Element(
        "posts-listing__item", By.CLASS_NAME))

    article_general_element: Element = field(
        default=Element("article", By.TAG_NAME))

    news_content_element: Element = field(
        default=Element("post-content", By.CLASS_NAME))

    next_news_btn: Element = field(default=Element(
        "//button[8]//*[name()='svg']", By.XPATH))

    category_element: Element = field(
        default=Element("post-cover__badge", By.CLASS_NAME))

    headline_element: Element = field(
        default=Element("post__title", By.CLASS_NAME))

    subheadline_element: Element = field(
        default=Element(name="h2", type=By.TAG_NAME))

    authors_element: Element = field(
        default=Element(name="post-meta__author-name", type=By.CLASS_NAME))

    create_date_and_time_element: ElementAttr = field(
        default=Element(name="post-meta__publish-date", type=By.CLASS_NAME))

    update_date_and_time_element: Element = field(
        default=Element(name="post-meta__publish-date", type=By.CLASS_NAME))

    sleep_time_change_tab: float = field(default=0.5)

    hrefs_to_ignore: List[str] = field(
        default_factory=lambda: [""])

    cut_last_news_paragraphs: int = field(default=0)
    cut_last_news_headers: int = field(default=0)

    max_news_text_len: int = field(default=700)

    no_views_element: Element = field(
        default=Element(name="(//span[@class='post-actions__item-count'])[1]", type=By.XPATH))

    # there are no comments on Cointelegraph
    no_comments_element: Element = field(
        default=Element(name="", type=By.XPATH))

    def parse_authors(self, authors: str) -> List[str]:
        return authors

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
        if ('HOURS' in input_datetime) | ('MINUTES' in input_datetime):
            to_return = datetime.now().strftime("%Y-%m-%d 00:00:00")
        else:
            to_return = datetime.strptime(input_datetime, "%b %d, %Y").strftime("%Y-%m-%d 00:00:00")
        print(to_return)
        return to_return
