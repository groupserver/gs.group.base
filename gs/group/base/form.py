# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from gs.content.form.form import SiteForm


class GroupForm(SiteForm):
    def __init__(self, context, request):
        super(GroupForm, self).__init__(context, request)

    @Lazy
    def groupInfo(self):
        retval = createObject('groupserver.GroupInfo', self.context)
        return retval
