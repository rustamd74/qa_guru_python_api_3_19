import os
import allure

from selene import have

EMAIL = os.getenv('EMAIL')


def test_auth_login(auth_user):
    with allure.step('Checking for Successful Authorization'):
        auth_user.open('')
        auth_user.element('.account').should(have.text(EMAIL))


def test_add_to_cart(auth_user):
    with allure.step('Product selection'):
        auth_user.open('/notebooks')
    with allure.step("Add to cart"):
        auth_user.element('.button-2 ').click()
    with allure.step('Check Add to Cart'):
        auth_user.element('.content').should(have.text('The product has been added to your '))


def test_checking_shopping_cart(auth_user):
    with allure.step('Checking shopping cart'):
        auth_user.open('/cart')
        auth_user.element('.product-name').should(have.text('Laptop'))


def test_update_shopping_cart(auth_user):
    with allure.step('Selecting product in cart'):
        auth_user.open('')
        auth_user.element('.ico-cart').click()
    with allure.step('Removing an item from the cart'):
        auth_user.element('.qty-input').clear().send_keys(0).press_enter()
    with allure.step('Checking if the cart is empty'):
        auth_user.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_logout(auth_user):
    with allure.step('Checking the logout'):
        auth_user.open('')
        auth_user.element('.ico-logout').click()
    with allure.step('Exit check'):
        auth_user.element('.ico-login').should(have.text('Log in'))
