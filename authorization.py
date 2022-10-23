import time
from pullgerInternalControl import pullgerFootPrint


def acceptance_of_questions(squirrel):
    alert_element = squirrel.find_xpath(xpath="//section[@class='artdeco-global-alert__body']")
    if alert_element is not None:
        accept_button = alert_element.find_xpath(xpath="//button[@action-type='ACCEPT']")
        if accept_button is not None:
            accept_button.click()
        else:
            raise pullgerFootPrint.ElementNotFound(
                msg="Unknown alert structure",
                level=30
            )

    pass


def get_password_input_element(squirrel):
    # Return password input element

    password_field = squirrel.find_xpath(xpath="//input[@id='session_password']")
    if password_field is None:
        password_field = squirrel.find_xpath(xpath="//input[@id='password']")

    return password_field


def get_sing_in_button(squirrel):
    # Return submit button

    submit_button = squirrel.find_xpath(xpath="//button[@class='sign-in-form__submit-button']")
    if submit_button is None:
        submit_button = squirrel.find_xpath(xpath="//button[@data-litms-control-urn='login-submit']")

    return submit_button


def get_user_input_element(squirrel):
    # Username field for authorization

    user_input_field = squirrel.find_xpath(xpath="//input[@id='session_key']")
    if user_input_field is None:
        user_input_field = squirrel.find_xpath(xpath="//input[@id='username']")

    return user_input_field


def set_password(squirrel, password: str):
    # Set password in field

    password_input_element = get_password_input_element(squirrel)
    if password_input_element is not None:
        password_input_element.send_string(password)
    else:
        raise pullgerFootPrint.ElementNotFound(
            msg="Password input element not found",
            level=30
        )


def set_user_name(squirrel, user_name: str):
    # Set up username

    userInput = get_user_input_element(squirrel=squirrel)

    if userInput is not None:
        userInput.send_string(user_name)
    else:
        raise pullgerFootPrint.ElementNotFound(
            msg="User name field not found",
            level=30
        )


def goto_login_page(squirrel):
    # Goto login page

    squirrel.get(url="https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


def sing_in(squirrel):
    # Push submit button

    sing_in_button = get_sing_in_button(squirrel)
    if sing_in_button is not None:
        time.sleep(1)
        sing_in_button.click()
    else:
        raise pullgerFootPrint.ElementNotFound(
            msg="Submit button do not found.",
            level=40
        )
