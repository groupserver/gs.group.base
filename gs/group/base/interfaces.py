# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals
from zope.interface import Interface
from zope.schema import Field
from Products.XWFChat.interfaces import IGSGroupFolder


class IGSGroupMarker(IGSGroupFolder):
    '''The base marker-interface for groups.'''


# TODO: Create a field type for siteInfo and groupInfo instances.
class IGSGroupPage(Interface):
    siteInfo = Field(title='Site Information',
        description='A SiteInfo instance.',
        required=True)

    groupInfo = Field(title='Group Information',
        description='GroupInfo instance.',
        required=True)
