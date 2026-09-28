from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import url
import locators
import data

def test_create_advertisement_without_authorization(driver):
    driver.get(url.BASE_URL)

    # Нажимаем кнопку «Разместить объявление»
    driver.find_element(
        *locators.PLACE_ADVERTISEMENT_BUTTON
    ).click()

    # Ждём появления модального окна
    modal = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            locators.AUTHORIZATION_REQUIRED_MODAL
        )
    )

    # Ждём появления заголовка
    title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            locators.AUTHORIZATION_REQUIRED_TITLE
        )
    )

    # Проверяем отображение модального окна
    assert modal.is_displayed()

    # Проверяем текст заголовка
    assert title.text == "Чтобы разместить объявление, авторизуйтесь"


# Тест сам регистрирует пользователя вместо использования заранее созданного аккаунта.
# Это решает проблему пагинации, но формально отличается от исходного сценария.
def test_create_advertisement_by_authorized_user(driver):
    driver.get(url.BASE_URL)

    # Генерируем данные один раз и используем их для регистрации и входа.
    email = data.generate_email()
    password = data.generate_password()
    wait = WebDriverWait(driver, 10)

    # Регистрируем нового пользователя, у которого ещё нет объявлений.
    wait.until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(locators.REGISTRATION_PASSWORD_CONFIRMATION_INPUT))
    driver.find_element(*locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REGISTRATION_PASSWORD_CONFIRMATION_INPUT).send_keys(password)
    driver.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()
    wait.until(EC.visibility_of_element_located(locators.USER_AVATAR))

    # Выходим, чтобы затем проверить вход с теми же данными.
    wait.until(EC.element_to_be_clickable(locators.LOGOUT_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON))

    # Переход к форме авторизации
    driver.find_element(
        *locators.LOGIN_AND_REGISTRATION_BUTTON
    ).click()

    # Ждём готовности формы авторизации
    email_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.LOGIN_EMAIL_INPUT)
    )

    # Авторизуемся
    email_input.send_keys(email)
    driver.find_element(
        *locators.LOGIN_PASSWORD_INPUT
    ).send_keys(password)

    driver.find_element(*locators.LOGIN_BUTTON).click()

    # Ждём успешной авторизации
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locators.USER_AVATAR)
    )

    # Переходим к созданию объявления
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            locators.PLACE_ADVERTISEMENT_BUTTON
        )
    ).click()

    # Генерируем уникальное название объявления
    advertisement_title = data.generate_advertisement_title()

    # Заполняем название
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            locators.ADVERTISEMENT_TITLE_INPUT
        )
    ).send_keys(advertisement_title)

    # Заполняем описание
    driver.find_element(
        *locators.ADVERTISEMENT_DESCRIPTION_INPUT
    ).send_keys(data.ADVERTISEMENT_DESCRIPTION)

    # Заполняем стоимость
    driver.find_element(
        *locators.ADVERTISEMENT_PRICE_INPUT
    ).send_keys(data.ADVERTISEMENT_PRICE)

    # Выбираем категорию
    driver.find_element(
        *locators.ADVERTISEMENT_CATEGORY_DROPDOWN
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            locators.ADVERTISEMENT_CATEGORY_OPTION
        )
    ).click()

    # Выбираем город
    driver.find_element(
        *locators.ADVERTISEMENT_CITY_DROPDOWN
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            locators.ADVERTISEMENT_CITY_OPTION
        )
    ).click()

    # Выбираем состояние товара
    driver.find_element(
        *locators.ADVERTISEMENT_CONDITION_RADIO_BUTTON
    ).click()

    # Публикуем объявление
    driver.find_element(
        *locators.PUBLISH_ADVERTISEMENT_BUTTON
    ).click()

    # Ждём закрытия формы создания объявления
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(
            locators.PUBLISH_ADVERTISEMENT_BUTTON
        )
    )

    # Переходим в профиль пользователя
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            locators.USER_PROFILE_BUTTON
        )
    ).click()

    # Ждём перехода в профиль
    WebDriverWait(driver, 10).until(
        EC.url_contains("/profile")
    )

    # Ждём появления блока «Мои объявления»
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            locators.MY_ADVERTISEMENTS_SECTION
        )
    )

    # Получаем названия объявлений пользователя
    advertisement_titles = WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located(
            locators.MY_ADVERTISEMENT_TITLES
        )
    )

    # Проверяем, что созданное объявление есть в профиле
    assert advertisement_title in [
        title.text for title in advertisement_titles
    ]
