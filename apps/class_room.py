__author__ = 'windy'
#coding: utf-8
from base import *
from wxt_api import *
from datetime import datetime

#===============================后台管理=====================

@Route("/virtualClassRoom/(.*)/student", name="Student Join")
class StudentJoinHandle(BaseHandler):
    def get(self, uid=''):
        join_url = room_dispatch(cid='6878082500', uid=uid)
        self.render("admin/wxt_vc.html", join_url=join_url)


@Route("/virtualClassRoom/teacher", name="Teacher Join")
class TeacherJoinHandle(BaseHandler):
    def get(self):
        uid = self.get_argument("uid", '7632351460')
        cid = self.get_argument("cid", '6878082500')
        now = datetime.now()
        course_update_start_time(cid=cid, start_time=now.strftime("%Y-%m-%d %H:%m"), length="45")
        join_url = room_dispatch(uid=uid, cid=cid)
        self.render("admin/wxt_vc.html", join_url=join_url)
