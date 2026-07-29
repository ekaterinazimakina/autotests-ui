import allure

@allure.step("Open browser")
def open_browser():
    with allure.step("Get browser"):
        ...
    with allure.step("Start browser"):
        with allure.step("Get browser"):
            ...

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ...

@allure.step("Close browser")
def close_browser():
    ...


def test_feature():
    open_browser()

    create_course()

    close_browser()