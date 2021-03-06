#coding:UTF-8
__author__ = 'windy'
import urllib
import urllib2
import httplib
import ujson
import traceback
import smtplib
import tornado.web
# from torndb import Row
from tornado.web import gen_log
from urllib2 import Request, urlopen

class Row(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


class Route(object):
    """
    Example
    -------

    @route('/some/path')
    class SomeRequestHandler(RequestHandler):
        pass

    @route('/some/path', name='other')
    class SomeOtherRequestHandler(RequestHandler):
        pass

    my_routes = route.get_routes()

    In your Application:
    Application = Application(my_routes, **settings)
    """
    _routes = []

    def __init__(self, uri, name=None):
        self._uri = uri
        self.name = name

    def __call__(self, _handler):
        """gets called when we class decorate"""
        name = self.name and self.name or _handler.__name__
        self._routes.append(tornado.web.url(self._uri, _handler, name=name))
        return _handler

    @classmethod
    def get_routes(cls):
        return cls._routes


def route_redirect(from_, to, name=None):
    Route._routes.append(tornado.web.url(from_, tornado.web.RedirectHandler, dict(url=to), name=name))


def nice_bool(value):
    if type(value) is bool:
        return value
    false = ('', 'no', 'off', 'false', 'none', '0', 'f')
    return str(value).lower().strip() not in false


def http_post(host, api, method, param, headers):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request(method, api, param, headers)
        res = conn.getresponse()
        data = res.read()
        conn.close()
        return data
    except:
        gen_log.info(traceback.format_exc())
        return False


def post_u8(url, data, headers):
    data = urllib.urlencode(data)
    req = Request(url, data=data, headers=headers)
    return urlopen(req).read()


def post(url, data):
    req = Request(url)
    data = urllib.urlencode(data)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()


def post2(data):
    conn = httplib.HTTPConnection('10.19.1.130', 10087)
    headers = {'Content-type': 'text/plain;charset=GBK'}
    conn.request('POST', '/CPAPlatform/TransformData', data, headers)
    response = conn.getresponse()
    print response.read()
    resp_data = response.read().decode('GBK').encode('UTF-8')
    return Row(ujson.loads(resp_data))


class CheckRoll(object):
    NORMAL = 0
    FINISHED = 1
    LOCKED = 2
    LATE = 3
    ABSENT = 4
    CHANGE = 6
    NAME = {
        0: "等待上课",
        1: "完成",
        2: "预考勤",
        3: "迟到",
        4: "缺席",
        6: "已调课",
        7: "调试课",
    }
    TRAIL = 7


def list_page(display, p_count, p_no):
    x, y = 1, p_count
    rount = p_count - display + 1
    if rount > 0:
        if rount > display:
            if display <= p_no <= rount:
                x = p_no
                y = display + p_no - 1
            elif rount < p_no <= p_count:
                x = rount
                y = p_count
            else:
                x = 1
                y = display
        else:
            if p_no >= display:
                x = rount
                y = p_count
            else:
                x = 1
                y = display
    return range(x, y + 1)

