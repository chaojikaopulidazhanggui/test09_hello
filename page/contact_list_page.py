from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactListPage(BaseAction):

    # 添加联系人按钮
    add_contact_button = By.ID, "com.android.contacts:id/floating_action_button"

    # 点击添加联系人
    def click_add_contact(self):
        self.click(self.add_contact_button)

