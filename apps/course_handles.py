__author__ = 'windy'
#coding: utf-8
from base import *


#===============================后台管理=====================

@Route("/admin", name="Admin")
class UserHandle(BaseHandler):
    def get(self):
        self.render("admin/index.html")
