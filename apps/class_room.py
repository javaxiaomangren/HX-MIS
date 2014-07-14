__author__ = 'windy'
#coding: utf-8
from base import *
from wxt_api import *
import datetime as dt
from datetime import datetime

#===============================后台管理=====================


@Route("/virtualClassRoom/(.*)/student", name="Student Join")
class StudentJoinHandle(BaseHandler):
    def get(self, uid=''):
        try:
            with open("courses", 'r') as f:
                lines = f.readlines()
                line = lines[0][:-1]
                arrange_student(uid, line)
                join_url = room_dispatch(cid=line, uid=uid)
                self.render("admin/wxt_vc.html", join_url=join_url)
        except:
            self.write("no class Info")

@Route("/virtualClassRoom/teacher", name="Teacher Join")
class TeacherJoinHandle(BaseHandler):
    def get(self):
        uid = self.get_argument("uid", '3714276568')
        # cid = self.get_argument("cid", '6878082500')
        dt_str = dt.datetime.now().strftime("%Y-%m-%d %H:%m")
        logger.info(dt_str)
        rs = course_create(title='Trial Class at ' + dt_str, c_type='1', length='45', start_time=dt_str)
        cs = course = str(rs.get("course").get("uniqueCourseId"))
        logger.info(cs)
        arrange_teacher(course, uid)
        with open("courses", 'w') as f:
            f.write(course + '\n')
        # course_update_start_time(cid=course, start_time=now.strftime("%Y-%m-%d %H:%m"), length="45")
        join_url = room_dispatch(uid=uid, cid=course)
        self.render("admin/wxt_vc.html", join_url=join_url)
