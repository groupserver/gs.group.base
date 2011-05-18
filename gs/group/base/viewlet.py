# coding=utf-8
from contentprovider import GroupContentProvider

class GroupViewlet(GroupContentProvider):
    def __init__(self, group, request, view, manager):
        GroupContentProvider.__init__(self, group, request, view)
        self.manager = manager

