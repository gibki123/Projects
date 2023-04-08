from dataclasses import dataclass, field
from typing import List
from selenium.webdriver.common.by import By


@dataclass(frozen=True)
class ElonMusk:
    url: str = field(default="https://twitter.com/elonmusk")

    close_popups: bool = field(default=True)
    popup_names: List[str] = field(default_factory=lambda: ["/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]",
                                                            ])
    popup_types: List[str] = field(default_factory=lambda: [By.XPATH])
    times_popup_waiting: List[str] = field(default_factory=lambda: [1])

    login_button: str = field(default="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/div[1]/span[1]/span[1]")

    mail_input: str = field(default="//input[@name='text']")
    next_login_button: str = field(default="//span[contains(text(),'Dalej')]")

    phone_input: str = field(default="//input[@name='text']")
    next_phone_button: str = field(default="//span[contains(text(),'Dalej')]")

    password_input: str = field(default="//input[@name='password']")
    final_login_button: str = field(default="//span[@class='css-901oao css-16my406 css-bfa6kz r-poiln3 r-1inkyih r-rjixqe r-bcqeeo r-qvutc0']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][contains(text(),'Zaloguj się')]")

    main_tweets_region: str = field(default="//section[@role='region']")