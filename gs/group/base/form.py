# coding=utf-8
from zope.component import createObject
try:
    from five.formlib.formbase import PageForm
except ImportError:
    from Products.Five.formlib.formbase import PageForm

class GroupForm(PageForm):
    def __init__(self, context, request):
        PageForm.__init__(self, context, request)
        self.__siteInfo = None
        self.__groupInfo = None
    
    @property
    def groupInfo(self):
        if self.__groupInfo == None:
            self.__groupInfo = \
                createObject('groupserver.GroupInfo', self.context)
        return self.__groupInfo

    @property
    def siteInfo(self):
        if self.__siteInfo == None:
            self.__siteInfo = \
                createObject('groupserver.SiteInfo', self.context)
        return self.__siteInfo

