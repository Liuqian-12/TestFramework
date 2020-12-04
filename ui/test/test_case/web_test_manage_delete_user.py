# coding=utf-8

import sys
import os
import time
import unittest
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from ui.view.businessview.web.common.login_business import simple_login
from ui.view.businessview.web.admin.manage_deleted_users_business import *
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path


class web_test_manage_delete_user(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
    
    def test_admin_page(self):
        self.driver = simple_login()
        self.data = Yaml(web_config_path).read()
        self.env = self.data['env']
        adminUrl = self.data['portal'][self.env] + "/admin"
        self.driver.get(adminUrl)

        # try:
        manage_del_user = Manage_deleted_users_business(self.driver)
        # manage_del_user.click_settings_button()
        # manage_del_user.click_admin_link()
        # title = self.driver.title
        # self.assertEqual(title, "Admin settings | Microsoft Stream", "当前在admin settings页面！")
        manage_del_user.admin_settings_page()
        # 验证是否在manage_del_users模块
        self.assertTrue(manage_del_user.assert_manage_del_users_model("aria-selected") == "true", "Enter manage_deleted_users_model, Failed!!!")
        # 搜索关键字：test
        manage_del_user.search("test")
        manage_del_user.icon_edit()
        # 验证点击edit按钮是否成功进入edit user details页面
        self.assertIn("Edit user details", manage_del_user.assert_is_edit_user_details_page(), "Edit user details, Failed!!!")
        manage_del_user.edit_user_details("test_user")
        manage_del_user.save_edit()
        manage_del_user.edit_cancel()
        manage_del_user.delete_button()
        manage_del_user.cancel_delete_button()
     
        # except Exception:
        #     self.save_img("test_manage_deleted_users-test_error1-screenshot1")
    
    
if __name__ == "__main__":
    unittest.main()
    
