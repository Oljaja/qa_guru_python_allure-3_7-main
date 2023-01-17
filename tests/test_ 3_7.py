import allure
from allure_commons.types import Severity, AttachmentType
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'ivanova')
@allure.severity(Severity.NORMAL)
@allure.feature('Проверка названия Issue в репозитории через Web-интерфейс')
@allure.story('Чистый selene')
@allure.link('https://github.com', name='Тестирование')
def test_selene():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#76')).should(be.visible)
    browser.quit()


@allure.tag('web')
@allure.label('owner', 'ivanova')
@allure.severity(Severity.NORMAL)
@allure.feature('Проверка названия Issue в репозитории через Web-интерфейс')
@allure.story('Лямбда шаги через with allure.step')
@allure.link('https://github.com', name='Тестирование')
def test_gitub():
    with allure.step('Открываем главную страницу'):
        browser.config.window_height = 1920
        browser.config.window_width = 1620
        browser.open('https://github.com/')
    with allure.step('Найти репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()
    with allure.step('Открыть репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Открыть таб issues'):
        browser.element('#issues-tab').click()
    with allure.step('Проверить наличие issue с номером 76'):
        browser.element(by.partial_text('#76')).should(be.visible)
    with allure.step("Делаем скриншот"):
        allure.attach(browser.driver.get_screenshot_as_png(), name="picture", attachment_type=AttachmentType.PNG)
    browser.quit()


@allure.tag('web')
@allure.label('owner', 'ivanova')
@allure.severity(Severity.NORMAL)
@allure.feature('Проверка названия Issue в репозитории через Web-интерфейс')
@allure.story('Шаги с декоратором @allure.step')
@allure.link('https://github.com', name='Тестирование')
def test_decorator():
    main_page()
    find_repo('eroshenkoam/allure-example')
    open_repo('eroshenkoam/allure-example')
    issue_click()
    issue()


@allure.step('Открываем главную страницу')
def main_page():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com/')


@allure.step("Найти репозиторий {repo}")
def find_repo(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repo).press_enter()


@allure.step("Открыть {repo}")
def open_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открыть таб issues')
def issue_click():
    browser.element('#issues-tab').click()


@allure.step('Проверить наличие issue с номером 76')
def issue():
    browser.element(by.partial_text('#76')).should(be.visible)


browser.quit()
