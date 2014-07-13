__author__ = 'windy'
#coding:utf-8
import time
import hashlib
from utils import http_post
import ujson

# """
# wxtapi.wangxiaotong.com
# 校长帐号 wxtapi@163.com 密码 123456
# uniqueUserId	7602270640
# partner	20140327173227
# appKey	25968f684db04d409ca3ab8d91da9609
# """


wxt_url = "http://api.wangxiaotong.com"
partner = "20140327173227"
appkey = "25968f684db04d409ca3ab8d91da9609"
_headers = {"Content-type": "application/x-www-form-urlencoded"}
post = "POST"
host = "api.wangxiaotong.com"


def get_http_result(rs):
    if rs:
        return ujson.loads(rs)
    else:
        return {"success": False, "error": "http request error"}


def student_create(uname='', nickname='', pw='', valid_period='1', pic_url='', email='', tel=''):
    """
    创建学生
    valid_period: 学生有效期类型, 可选值为 1、7、 15、30、60、90、180、360
    """
    timestamp = str(int(time.time()*1000))
    if not isinstance(nickname, unicode):
        nickname = nickname.decode('utf8').encode('utf8')
    params = 'nickname='+nickname + \
             '&partner=' + partner + \
             '&passwd=' + pw + \
             '&timestamp=' + timestamp + \
             '&username=' + uname + \
             '&validPeriodType=' + valid_period
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, "/api/student/create", post, params + "&sign=" + sign, headers=_headers)
    return get_http_result(rs)
    #{"student":{"uniqueUserId":2450576060,"username":"abc124","nickname":"李华",
    # "email":null,"mobile":null,"validStartTime":"2014-07-12 17:11:51",
    # "validEndTime":"2014-07-13 23:59:59","validPeriodType":1,
    # "avatarUrl":"http://avatar.wangxiaotong.com/avatar/20130730/7534c9996e37470990265fccb961886e.jpg"},
    # "error":"user_exitst_error","success":false}


def student_extend(uid='', valid_period='1'):

    """
    激活或者延长学生有效期
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueUserId=' + uid + \
             '&validPeriodType=' + valid_period

    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/student/extend', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)
    # {u'success': True, u'validendTime': u'2014-07-20 23:59:59', u'validStartTime': u'2014-07-12 17:11:51'}


def teacher_create(uname='', pw='', nickname=''):
    """创建老师"""
    timestamp = str(int(time.time()*1000))
    #TODO TEST
    if not isinstance(nickname, unicode):
        nickname = nickname.decode('utf8').encode('utf8')
    params = 'nickname=' + nickname + \
             '&partner=' + partner + \
             '&passwd=' + pw + \
             '&timestamp=' + timestamp + \
             '&username=' + uname
    sign = hashlib.md5(params + appkey).hexdigest()
    print params + "&sign=" + sign
    rs = http_post(host, "/api/teacher/create", post, params + "&sign=" + sign, headers=_headers)
    return get_http_result(rs)
    # print teacher_create(uname='1234566', pw='123409', nickname='杨老师2')
    #{u'teacher': {u'username': u'1234566', u'avatarUrl': u'http://avatar.wangxiaotong.com/avatar/20130730/41072c18982240dd83dca3f7152a8df7.jpg', u'mobile': None, u'nickname': u'\u6768\u8001\u5e082', u'email': None, u'uniqueUserId': 4030584640L}, u'success': True}


def update_nickname(uid='', nickname=''):
    """
     更新老师和学生昵称
    """
    timestamp = str(int(time.time()*1000))
    params = 'nickname=' + nickname + \
             '&partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueUserId=' + uid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/user/update/nickname', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)
# print update_nickname(uid='2450576060', nickname='Student One')


def update_avatar(uid='', pic_url=''):
    """
    更新老师和学生头像 api
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&picUrl=' + pic_url + \
             '&timestamp=' + timestamp + \
             '&uniqueUserId=' + uid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/user/update/avatar', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def course_create(title='', c_type='1', length='30', start_time=''):
    """
    创建课程
    length: 课程时长,单位分钟, 可选值为 15, 30, 45, 60 ,90 ,120 ,150 ,180
    start_time: 课程开始时间,格式 2013-10-27 11:11
    """
    timestamp = str(int(time.time()*1000))
    params = 'courseLength=' + length + \
             '&courseType=' + c_type + \
             '&partner=' + partner + \
             '&startTime=' + start_time + \
             '&timestamp=' + timestamp + \
             '&title=' + title
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/create', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)
    # {u'course': {u'endTime': u'2014-07-13 11:30:00', u'uniqueCourseId': 1201363556, u'courseType': 1, u'startTime': u'2014-07-13 11:00:00', u'title': u'\u6691\u671f\u82f1\u8bed'}, u'success': True}


def course_update_title(cid='', title=''):
    """
    更新课程标题
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&title=' + title + \
             '&uniqueCourseId=' + cid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/update/title', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def course_update_start_time(cid='', start_time='', length='30'):
    """
    更新课程开始时间和时长
    length: 15, 30, 45, 60 ,90 ,120 ,150 ,180
    """
    timestamp = str(int(time.time()*1000))
    params = 'courseLength=' + length + \
             '&partner=' + partner + \
             '&startTime=' + start_time + \
             '&timestamp=' + timestamp + \
             '&uniqueCourseId=' + cid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/update/startTime', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def course_rm_student(cid='', uid=''):
    """
    把学生移除课程
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueCourseId=' + cid + \
             '&uniqueUserId=' + uid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/remove_student', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def course_delete(cid=''):
    """
    删除课程
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueCourseId=' + cid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/delete', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def upload_slide(uid, file_rs):
    """
    上传课件
    上传的用户 uniqueUserId,只有老师 和教务能够上传课件
    课件文件, 这个 api 比较特殊,参数加密时 不需要带上 slidesFile; 并且使用文件 流的格式上传
    """
    #TODO upload slide
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueUserId=' + uid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/delete', post, params + '&slidesFile' + file_rs + '&sign=' + sign, _headers)
    return get_http_result(rs)


def arrange_student(uid='', cid=''):
    """
    给学生排课
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueCourseId=' + cid + \
             '&uniqueUserId=' + uid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/arrange_student', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def arrange_teacher(cid='', tid=''):
    """
    给老师排课
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueCourseId=' + cid + \
             '&uniqueUserId=' + tid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/arrange_teacher', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def arrange_slides(cid='', sid=''):
    """
    给课件排课
    """
    timestamp = str(int(time.time()*1000))
    params = 'partner=' + partner + \
             '&timestamp=' + timestamp + \
             '&uniqueCourseId=' + cid + \
             '&slidesUuid=' + sid
    sign = hashlib.md5(params + appkey).hexdigest()
    rs = http_post(host, '/api/course/arrange_slides', post, params + '&sign=' + sign, _headers)
    return get_http_result(rs)


def room_dispatch(cid='', uid=''):
    """
    调度进直播教室
    地址: /api/room/dispatch
    请求方式: GET , 必须使用浏览器发出请求,因为会有 session 的校验
    @uni_uid:  1. 被排课学生或者老师的用户 uniqueUserId;
               2. 当使用校长的 uniqueUserId 时, 可以隐身进入课程查看课程情 况,不需要事前排课。
    @return Html , 返回一个教室 html。 教室的尺寸大小是 1040 * 600。可以针对这 个尺寸做自己适合的嵌入

    """
    timestamp = str(int(time.time()*1000))
    param = "partner=%s&timestamp=%s&uniqueCourseId=%s&uniqueUserId=%s" % (partner, timestamp, cid, uid)
    sign = hashlib.md5(param + appkey).hexdigest()
    return "http://api.wangxiaotong.com/api/room/dispatch?" + param + "&sign=" + sign


def record_dispatch(cid='', uid=''):
    """
    调度进回放教室
    """
    timestamp = str(int(time.time()*1000))
    param = "partner=%s&timestamp=%s&uniqueCourseId=%s&uniqueUserId=%s" % (partner, timestamp, cid, uid)
    sign = hashlib.md5(param + appkey).hexdigest()
    return "http://api.wangxiaotong.com/api/record/dispatch?" + param + "&sign=" + sign


