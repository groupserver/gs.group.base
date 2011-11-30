# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from AccessControl import getSecurityManager
from gs.viewlet.contentprovider import SiteContentProvider

class GroupContentProvider(SiteContentProvider):
    def __init__(self, group, request, view):
        SiteContentProvider.__init__(self, group, request, view)
        self.__parent__ = view
        self.__updated = False

    @Lazy
    def groupInfo(self):
        retval = createObject('groupserver.GroupInfo', self.context)
        return retval
        
    @Lazy
    def viewTopics(self):
        # --=mpj17=-- If the user can view the messages the he or she
        #   can view almost all of the sub-pages. This is *mostly* used
        #   to tell the difference between a Public and Private group.
        #   (Non-members cannot even see a Secret group, so it is not
        #   much of an issue.)
        #
        # TODO: Figure out I could do this better.
        msgs = self.context.messages
        user = getSecurityManager().getUser()
        retval = bool(user.has_permission('View', msgs))
        return retval

    @Lazy
    def isAnnouncement(self):
        template = self.groupInfo.get_property('group_template')
        return template == 'announcement'

