# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from gs.content.base.page import SitePage


class GroupPage(SitePage):
    def __init__(self, group, request):
        super(GroupPage, self).__init__(group, request)
        self.group = group

    @Lazy
    def groupInfo(self):
        retval = createObject('groupserver.GroupInfo', self.group)
        return retval
