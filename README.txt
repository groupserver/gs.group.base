Introduction
============

The code that defines the core of GroupServer_ groups. It defines the core
`marker interface`_ for a group, and the `base classes`_ for the pages that
make up a group.

Marker Interface
================

A folder is considered a group if it has the ``IGSGroupMarker`` marker
interface. For historical reasons this marker interface has the following
inheritance tree::

  Products.XWFChat.interfaces.IGSGroupFolder
      △
      │
  gs.group.base.interfaces.IGSGroupMarker

In the future the inheritance from ``IGSGroupFolder`` will be removed.

Base Classes
============

For base classes are provided: `GroupPage`_, `GroupForm`_,
`GroupContentProvider`_, and `GroupViewlet`_.

``GroupPage``
-------------

The ``gs.group.base.GroupPage`` class is a ``BrowserView`` that defines a
``siteInfo`` and ``groupInfo`` property [#page]_. It can be used in a ZCML
page declaration as-is::

  <browser:page 
    for="gs.group.base.interfaces.IGSGroupMarker"
    name="index.html"
    class="gs.group.base.page.GroupPage"
    template="browser/templates/homepage.pt"
    permission="zope2.View"/>

``GroupForm``
-------------

The ``gs.group.base.GroupForm`` *abstract base class* that defines a
``siteInfo`` and ``groupInfo`` property [#form]_. It cannot be used as-is,
unlike the ``GroupPage``. Instead, forms within a group subclass
``GroupForm`` and define

* ``form_fields``
* ``label``, and
* ``template``.

For example::

  from zope.formlib import form
  from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
  from gs.group.base import GroupForm

  class GroupAdminForm(GroupForm):
      form_fields = form.Fields(IGroupAdminForm)
      label = u'A Group Admin Form Example'
      pageTemplateFileName = 'browser/templates/adminform.pt'
      template = ZopeTwoPageTemplateFile(pageTemplateFileName)

      def __init__(self, group, request):
          super(GroupAdminForm, self).__init__(group, request)

``GroupContentProvider``
------------------------

The ``gs.group.base.GroupContentProvider`` is a content provider that
defines a ``siteInfo`` and ``groupInfo`` property. It can be used as is, or
as the base of a viewlet.

``GroupViewlet``
----------------

The ``gs.group.base.GroupViewlet`` is a concrete class that defines a
``siteInfo`` and ``groupInfo`` property, inheriting them off the
`GroupContentProvider`_. It can be used in a ZCML viewlet_ declaration
as-is::

  <browser:viewlet 
    name="a-viewlet-name"
    for="gs.group.base.interface.IGSGroupMarker"
    manager="some.manager"
    template="browser/templates/a-viewlet-template.pt"
    class="gs.group.base.GroupViewlet"
    permission="zope.Public" />

TODO
====

The ``GroupInfo`` class should be moved into this egg from
``Products.GSGroup``.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.base
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#page] The ``GroupPage`` inherits most of its functionality from
           ``gs.content.base.page.SitePage``:
           <https://source.iopen.net/groupserver/gs.content.base/summary>
.. [#form] The ``GroupForm`` inherits most of its functionality from
           ``gs.content.form.SiteForm``:
           <https://source.iopen.net/groupserver/gs.content.form/summary>
.. _GroupServer: http://groupserver.org
.. _viewlet: http://docs.zope.org/zope.viewlet/
