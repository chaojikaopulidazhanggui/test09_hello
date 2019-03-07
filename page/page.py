from page.add_contact_page import AddContactPage
from page.contact_list_page import ContactListPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def add_contact(self):
        return AddContactPage(self.driver)

    @property
    def contact_list(self):
        return ContactListPage(self.driver)