# coding=utf-8
from zope.component import createObject
from gs.content.form.form import SiteForm

class GroupForm(SiteForm):
    def __init__(self, context, request):
        SiteForm.__init__(self, context, request)
        self.__groupInfo = None

    #TODO Use the zope.cachedescriptors.properties.Lazy decoration
    @property
    def groupInfo(self):
        if self.__groupInfo == None:
            self.__groupInfo = \
                createObject('groupserver.GroupInfo', self.context)
        return self.__groupInfo

