from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import data
import url
import locators

def test_user_registration(driver):
    # Подготовка тестовых данных
    email = data.generate_email()
    password = data.generate_password()

    driver.get(url.BASE_URL)

    # Переход к форме регистрации
    driver.find_element(*locators.LOGIN_AND_REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

    # Ждём, пока форма входа исчезнет
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(locators.NO_ACCOUNT_BUTTON)
    )
    # Ждём готовности формы регистрации
    email_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT)
    )

    # Заполнение формы регистрации
    email_input.send_keys(email)
    driver.find_element(*locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REGISTRATION_PASSWORD_CONFIRMATION_INPUT).send_keys(password)

    # Создание аккаунта
    driver.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()

    # Проверка успешной регистрации
    avatar = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locators.USER_AVATAR)
    )

    user_name = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locators.USER_NAME)
    )

    assert avatar.is_displayed()
    assert user_name.text == "User."


def test_registration_with_invalid_email(driver):
    # Подготовка тестовых данных
    email = data.generate_invalid_email()

    driver.get(url.BASE_URL)

    # Переход к форме регистрации
    driver.find_element(*locators.LOGIN_AND_REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)
    ).click()

     # Ждём, пока форма входа исчезнет
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(locators.NO_ACCOUNT_BUTTON)
    )

    # Ждём готовности формы регистрации
    email_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT)
    )

    # Вводим Email не по маске
    email_input.send_keys(email)

    # Создаём аккаунт
    driver.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()

    # Ждём появления ошибки
    email_error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locators.REGISTRATION_EMAIL_ERROR)
    )

    # Получаем контейнеры полей
    email_field = driver.find_element(
        *locators.REGISTRATION_EMAIL_FIELD_CONTAINER
    )
    password_field = driver.find_element(
        *locators.REGISTRATION_PASSWORD_FIELD_CONTAINER
    )
    password_confirmation_field = driver.find_element(
        *locators.REGISTRATION_PASSWORD_CONFIRMATION_FIELD_CONTAINER
    )

    # Проверяем сообщение об ошибке
    assert email_error.text == "Ошибка"

    # Проверяем красное оформление полей
    assert "inputError" in email_field.get_attribute("class")
    assert "inputError" in password_field.get_attribute("class")
    assert "inputError" in password_confirmation_field.get_attribute("class")


def test_registration_existing_user(driver):
    driver.get(url.BASE_URL)

    # Переход к форме регистрации
    driver.find_element(*locators.LOGIN_AND_REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)
    ).click()

    # Ждём завершения переключения на форму регистрации
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(locators.NO_ACCOUNT_BUTTON)
    )

    # Ждём готовности формы регистрации
    email_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT)
    )

    # Заполняем данные уже существующего пользователя
    email_input.send_keys(data.EXISTING_USER_EMAIL)

    driver.find_element(
        *locators.REGISTRATION_PASSWORD_INPUT
    ).send_keys(data.EXISTING_USER_PASSWORD)

    driver.find_element(
        *locators.REGISTRATION_PASSWORD_CONFIRMATION_INPUT
    ).send_keys(data.EXISTING_USER_PASSWORD)

    # Пытаемся создать аккаунт
    driver.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()

    # Ждём появления ошибки
    email_error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            locators.REGISTRATION_EMAIL_ERROR
        )
    )

    # Получаем контейнеры полей
    email_field = driver.find_element(
        *locators.REGISTRATION_EMAIL_FIELD_CONTAINER
    )

    password_field = driver.find_element(
        *locators.REGISTRATION_PASSWORD_FIELD_CONTAINER
    )

    password_confirmation_field = driver.find_element(
        *locators.REGISTRATION_PASSWORD_CONFIRMATION_FIELD_CONTAINER
    )

    # Проверяем сообщение об ошибке
    assert email_error.text == "Ошибка"

    # Проверяем красное оформление всех трёх полей
    assert "inputError" in email_field.get_attribute("class")
    assert "inputError" in password_field.get_attribute("class")
    assert "inputError" in password_confirmation_field.get_attribute("class")
