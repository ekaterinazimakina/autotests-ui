import allure

from components.base_component import BaseComponent

from playwright.sync_api import Page

from elements.text import Text

from elements.button import Button

class DeleteConfirmation(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'modal-title-text', 'Title')
        self.close_button = Button(page, 'modal-close-button', 'Close button')
        self.confirm_button = Button(page, 'modal-confirm-button', 'Confirm button')
        self.cancel_button = Button(page, 'modal-cancel-button', 'Cancel button')

    @allure.step('Check visible delete confirmation dialog')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Confirm deleting course')

        self.close_button.check_visible()

        self.confirm_button.check_visible()

        self.cancel_button.check_visible()

    def click_close_button(self):
        self.close_button.click()

    def click_confirm_button(self):
        self.confirm_button.click()

    def click_cancel_button(self):
        self.cancel_button.click()
