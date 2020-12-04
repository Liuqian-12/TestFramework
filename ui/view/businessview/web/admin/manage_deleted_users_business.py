# coding=utf-8
# @Time    :
# @Author  :
# @File    : manage_deleted_users_business.py
import time
from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.admin.manage_deleted_users_page import ManageDeletedUserPage as Page
from ui.lib.browser_engine import Logger


class Manage_deleted_users_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    # 获取元素属性值
    def assert_manage_del_users_model(self, text):
        return self.find_element(*self._page.manage_deleted_users).get_attribute(text)

    # 获取元素text值
    def assert_is_edit_user_details_page(self):
        return self.find_element(*self._page.edit_users_details).text
    
    # 点击settings按钮
    # def click_settings_button(self):
    #     time.sleep(2)
    #     self.click(self._page.setting_button)

    # 点击admin_settings按钮
    # def click_admin_link(self):
    #     element = self.find_element(*self._page.adminsettings_link)
    #     self.perform_javascript_click(element)
    #     time.sleep(1)
    #     self.switch_to_window_by_index(0)
    
    # 进入manage_deleted_users模块
    def admin_settings_page(self):
        self.click(self._page.manage_deleted_users)

    # find deleted users搜索框搜索
    def search(self, text):
        self.send_keys(self._page.search_delete_users, text, need_enter=True)

    # click edit button
    def icon_edit(self):
        time.sleep(2)
        edit_button = self.find_element(*self._page.edit_button)
        self.action_catena(edit_button, "单击")

    # click delete button
    def delete_button(self):
        time.sleep(2)
        delete_button = self.find_element(*self._page.delete_button)
        self.action_catena(delete_button, "单击")

    # cancel delete
    def cancel_delete_button(self):
        time.sleep(1)
        self.click(self._page.cancel_delete_button)

    # input name
    def edit_user_details(self, text):
        self.send_keys(self._page.edit_name, text)        

    # click save button
    def save_edit(self):
        time.sleep(1)
        self.click(self._page.save_edit_button)

    # cancel edit name
    def edit_cancel(self):
        self.icon_edit()
        time.sleep(1)
        self.click(self._page.cancel_edit_button)

    



    

        


        
        






        


        


    