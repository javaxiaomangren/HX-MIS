__author__ = 'windy'
#coding: utf-8
from base import *


#===============================后台管理=====================

@Route("/student/admin/create", name="Create WXT Student")
class StudentWxtHandle(BaseHandler):
    """
    添加网校通学生
    """
    def get(self):
        self.render("admin/student_wxt_form.html")

    def post(self, *args, **kwargs):
        pass

@Route("/teacher/admin/create", name="Create WXT Teacher")
class StudentWxtHandle(BaseHandler):
    """
    添加网校通老师
    """
    def get(self):
        self.render("admin/teacher_wxt_form.html")

    def post(self, *args, **kwargs):
        pass
