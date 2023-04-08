# TODO: Add config interface for tips in pycharm
from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass(frozen=True)
class Element:
    name: str
    type: By


@dataclass(frozen=True)
class ElementAttr(Element):
    attr: str


@dataclass(frozen=True)
class PopupElement(Element):
    time_waiting_s: float
