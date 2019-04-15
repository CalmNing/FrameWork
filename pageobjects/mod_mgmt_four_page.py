#  -*- coding: utf-8 -*-

from framework.basepage import BasePage
from framework.constans import Constans


class ModMgmtFourPage(BasePage):

    def click_jump(self):
        self.sleep(2)
        self.click(Constans.CLICK_JUMP)
