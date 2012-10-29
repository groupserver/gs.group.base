# coding=utf-8
from contentprovider import GroupContentProvider


class GroupViewlet(GroupContentProvider):
    def __init__(self, group, request, view, manager):
        super(GroupViewlet, self).__init__(group, request, view)
        self.manager = manager
