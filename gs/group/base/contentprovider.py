# coding=utf-8
from zope.component import createObject
from AccessControl import getSecurityManager

class GroupContentProvider(object):
    def __init__(self, group, request, view):
        self.__parent__ = self.view = view
        self.__updated = False

        self.context = group
        self.request = request
        self.__updated = False

        self.__siteInfo = None
        self.__groupInfo = None
        self.__viewTopics = None

    @property
    def siteInfo(self):
        if self.__siteInfo == None:
            self.__siteInfo = \
                createObject('groupserver.SiteInfo', self.context)
        return self.__siteInfo
        
    @property
    def groupInfo(self):
        if self.__groupInfo == None:
            self.__groupInfo = \
                createObject('groupserver.GroupInfo', self.context)
        return self.__groupInfo
        
    @property
    def viewTopics(self):
        # --=mpj17=-- If the user can view the messages the he or she
        #   can view almost all of the sub-pages. This is *mostly* used
        #   to tell the difference between a Public and Private group.
        #   (Non-members cannot even see a Secret group, so it is not
        #   much of an issue.)
        #
        # TODO: Figure out I could do this better.
        if self.__viewTopics:
            msgs = self.context.messages
            user = getSecurityManager().getUser()
            self.__viewTopics = bool(user.has_permission('View', msgs))
        return self.__viewTopics

