from selenium.webdriver.common.by import By

# Шапка главной страницы.

LOGIN_AND_REGISTRATION_BUTTON = (
    By.XPATH,
    ".//button[text()='Вход и регистрация']"
) # «Вход и регистрация».
PLACE_ADVERTISEMENT_BUTTON = (
    By.XPATH,
    ".//button[text()='Разместить объявление']"
) # «Разместить объявление».
USER_AVATAR = (
    By.XPATH,
    ".//button[@class='circleSmall']"
) # Аватар авторизованного пользователя.
USER_NAME = (
    By.XPATH,
    ".//h3[@class='profileText name']"
) # Имя пользователя: ожидаемый текст «User».
USER_PROFILE_BUTTON = (
    By.XPATH,
    ".//button[@class='circleSmall']"
)  # Элемент перехода в профиль
LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']") # кнопка «Выйти».


# Форма регистрации.

NO_ACCOUNT_BUTTON = (
    By.XPATH,
    ".//button[text()='Нет аккаунта']"
)  # «Нет аккаунта»: переход к регистрации.
REGISTRATION_EMAIL_INPUT = (By.XPATH, ".//input[@name='email']") # Поле Email.
REGISTRATION_PASSWORD_INPUT = (By.XPATH, ".//input[@name='password']") # Поле «Пароль».
REGISTRATION_PASSWORD_CONFIRMATION_INPUT = (
    By.XPATH,
    ".//input[@name='submitPassword']"
) # Поле «Повторите пароль».
CREATE_ACCOUNT_BUTTON = (
    By.XPATH,
    ".//button[text()='Создать аккаунт']"
) # «Создать аккаунт».
REGISTRATION_EMAIL_ERROR = (
    By.XPATH,
    ".//span[text()='Ошибка']"
)  # Сообщение «Ошибка» под полем Email.

# Контейнеры полей регистрации, на которых проверяется красное оформление.

REGISTRATION_EMAIL_FIELD_CONTAINER = (
    By.XPATH,
    ".//input[@name='email']/parent::div"
)
REGISTRATION_PASSWORD_FIELD_CONTAINER = (
    By.XPATH,
    ".//input[@name='password']/parent::div"
)
REGISTRATION_PASSWORD_CONFIRMATION_FIELD_CONTAINER = (
    By.XPATH,
    ".//input[@name='submitPassword']/parent::div"
)


# Форма авторизации.

LOGIN_EMAIL_INPUT = (By.XPATH, ".//input[@name='email']")  # Поле Email.
LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@name='password']")  # Поле «Пароль».
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # «Войти».

# Попытка разместить объявление без авторизации.
AUTHORIZATION_REQUIRED_MODAL = (
    By.XPATH,
    ".//form[contains(@class, 'popUp_shell')]"
)  # Модальное окно.
AUTHORIZATION_REQUIRED_TITLE = (
    By.XPATH,
    ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
)  # «Чтобы разместить объявление, авторизуйтесь».

# Форма создания объявления.

ADVERTISEMENT_TITLE_INPUT = (By.XPATH, ".//input[@name='name']")  # «Название».
ADVERTISEMENT_DESCRIPTION_INPUT = (By.XPATH, ".//textarea[@name='description']")  # «Описание товара».
ADVERTISEMENT_PRICE_INPUT = (By.XPATH, ".//input[@name='price']")  # «Стоимость».
ADVERTISEMENT_CATEGORY_DROPDOWN = (By.XPATH, ".//input[@name='category']/following-sibling::button")  # Список «Категория».
ADVERTISEMENT_CATEGORY_OPTION = (By.XPATH, ".//button[.//span[text()='Книги']]")  # Выбранная для теста категория в списке.
ADVERTISEMENT_CITY_DROPDOWN = (By.XPATH, ".//input[@name='city']/following-sibling::button")  # Список «Город».
ADVERTISEMENT_CITY_OPTION = (By.XPATH, ".//button[.//span[text()='Москва']]")  # Выбранный для теста город в списке.
ADVERTISEMENT_CONDITION_RADIO_BUTTON = (
    By.XPATH,
    ".//input[@name='condition' and @value='Б/У']/following-sibling::div"
)  # Выбранное «Состояние товара».
PUBLISH_ADVERTISEMENT_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")   # «Опубликовать».

# Профиль пользователя: поиск созданного объявления по его уникальному названию.

MY_ADVERTISEMENTS_SECTION = (
    By.XPATH,
    ".//h1[text()='Мои объявления']/parent::div"
) # Блок «Мои объявления».
MY_ADVERTISEMENT_CARDS = (
    By.XPATH,
    ".//h1[text()='Мои объявления']/parent::div//div[@class='card']"
) # Карточки внутри блока «Мои объявления».
MY_ADVERTISEMENT_TITLES = (
    By.XPATH,
    ".//h1[text()='Мои объявления']/parent::div//div[@class='about']/h2"
) # Названия объявлений внутри этого блока.
