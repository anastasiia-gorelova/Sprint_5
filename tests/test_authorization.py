from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import url
import locators
import data


def test_user_login(driver):
    driver.get(url.BASE_URL)

    # Переход к форме авторизации
    driver.find_element(*locators.LOGIN_AND_REGISTRATION_BUTTON).click()

    # Ждём готовности формы авторизации
    email_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.LOGIN_EMAIL_INPUT)
    )

    # Заполняем форму авторизации
    email_input.send_keys(data.EXISTING_USER_EMAIL)
    driver.find_element(
        *locators.LOGIN_PASSWORD_INPUT
    ).send_keys(data.EXISTING_USER_PASSWORD)

    # Нажимаем кнопку «Войти»
    driver.find_element(*locators.LOGIN_BUTTON).click()

    # Ждём появления аватара авторизованного пользователя
    avatar = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locators.USER_AVATAR)
    )

    # Ждём появления имени пользователя
    user_name = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locators.USER_NAME)
    )

    # Проверяем аватар и имя пользователя
    assert avatar.is_displayed()
    assert user_name.text == "User."


def test_user_logout(driver):
    driver.get(url.BASE_URL)

    # Переход к форме авторизации
    driver.find_element(*locators.LOGIN_AND_REGISTRATION_BUTTON).click()

    # Ждём готовности формы авторизации
    email_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.LOGIN_EMAIL_INPUT)
    )

    # Заполняем форму авторизации
    email_input.send_keys(data.EXISTING_USER_EMAIL)
    driver.find_element(
        *locators.LOGIN_PASSWORD_INPUT
    ).send_keys(data.EXISTING_USER_PASSWORD)

    # Нажимаем кнопку «Войти»
    driver.find_element(*locators.LOGIN_BUTTON).click()

    # Ждём появления кнопки «Выйти»
    logout_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.LOGOUT_BUTTON)
    )

    # Выходим из аккаунта
    logout_button.click()

    # Ждём появления кнопки «Вход и регистрация»
    login_button = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            locators.LOGIN_AND_REGISTRATION_BUTTON
        )
    )

    # Проверяем, что аватар и имя пользователя исчезли
    avatar_is_hidden = WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(locators.USER_AVATAR)
    )

    user_name_is_hidden = WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(locators.USER_NAME)
    )

    assert avatar_is_hidden
    assert user_name_is_hidden
    assert login_button.is_displayed()