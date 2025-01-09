from selene import browser, be, have


def test_first(google_open):
    browser.element('[id="L2AGLb"]').click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[class="LC20lb MBeuO DKV0Md"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_second(google_open):
    browser.element('[id="L2AGLb"]').click()
    browser.element('[name="q"]').should(be.blank).type('sewerser345345').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу sewerser345345 ничего не найдено.'))
https://github.com/Tnillion/getting-started-python.git
https://github.com/Tnillion/first_repo/getting-started-python.git/