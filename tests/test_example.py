def test_ya_ru_title(browser):
    browser.get("https://dzen.ru")
    assert "Дзен" in browser.title


def test_google_ru_title(browser):
    browser.get("https://google.com")
    assert "Google" in browser.title
