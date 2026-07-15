import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number, expected):
    assert number ** 2 == expected


@pytest.mark.parametrize('browser', ['chromiun', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['macos', 'linux', 'windows', 'debian'])
def test_multiplication_of_numbers(os, browser):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromiun', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations: {user}')

    def test_user_without_operations(self, user: str):
        print(f'User without operations: {user}')

users = {
    '+7000000567': 'user_with_money',
    '+7000000789': 'user_without_money',
    '+7000000987': 'user_with_operations'
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]} '
    )

def test_identifiers(phone_number: str):
    ...
