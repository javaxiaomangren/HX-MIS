__author__ = 'windy'
#coding: utf-8
import traceback
import ujson
import json
from datetime import datetime, timedelta
from utils import *
import sys
if sys.version_info < (2, 7):
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict

import tornado.web
from utils import Row
from tornado.log import gen_log as logger


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def db_model(self):
        return self.application.db_model

    def auto_commit(self, flag=True):
        self.db._db.autocommit(flag)

    def commit(self):
        self.db._db.commit()

    def rollback(self):
        self.db._db.rollback()

    def get_template_namespace(self):
        ns = super(BaseHandler, self).get_template_namespace()
        ns.update({
            'CheckRoll': CheckRoll,
            "get_pages": list_page
        })

        return ns

    # def get_current_user(self):
    #     user = self.get_secure_cookie("user_speiyou")
    #     row = self.db.get("SELECT role, password FROM user where username=%s", user)
    #     if row:
    #         return user
    #     return None

    def write_error(self, status_code, **kwargs):

        if status_code in [403, 404, 500, 503]:
            filename = '200.html'
            print 'rendering filename: ', filename
            return self.render_string(filename, entry=Row({"msg": "Wrong login"}))
        #
        # return "<html><title>%(code)d: %(message)s</title>" \
        #         "<body class='bodyErrorPage'>%(code)d: %(message)s</body>"\
        #         "</html>" % {
        #         "code": status_code,
        #         "message": httplib.responses[status_code],
        #         }

