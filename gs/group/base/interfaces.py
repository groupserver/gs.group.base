# coding=utf-8
from zope.interface import Interface
from zope.schema import Field

# TODO: Create a field type for siteInfo and groupInfo instances.
class IGSGroupPage(Interface):
    siteInfo = Field(title=u'Site Information',
        description=u'A SiteInfo instance.',
        required=True)

    groupInfo = Field(title=u'Group Information',
        description=u'A GroupInfo instance.',
        required=True)

