.. sectnum::

============
Introduction
============

The code that defines the core of GroupServer groups. Its primary job
is to define a `GroupPage`_, `GroupForm`_ and `GroupContentProvider`_.

``GroupPage``
=============

The ``gs.group.base.page.GroupPage`` class is a ``BrowserView`` that
defines a ``siteInfo`` and ``groupInfo`` property. It can be used in
a ZCML page declaration as-is::

    <browser:page 
    for="Products.XWFChat.interfaces.IGSGroupFolder"
    name="index.html"
    class="gs.group.base.page.GroupPage"
    template="browser/templates/homepage.pt"
    permission="zope2.View"/>

``GroupForm``
=============

The ``gs.group.base.form.GroupForm`` *abstract base class* is a
``PageForm`` that defines a ``siteInfo`` and ``groupInfo`` property. It
cannot be used as-is, unlike the ``GroupPage``. Instead, forms within a
group subclass ``GroupForm`` and define

* ``form_fields``
* ``label``, and
* ``template``.

``GroupContentProvider``
========================

The ``gs.group.base.contentprovider.GroupContentProvider`` is a content
provider that defines a ``siteInfo`` and ``groupInfo`` property. It can
be used as is, or as the base of a viewlet.

TODO
====

* The marker interface for groups will be moved into this module
  [#Marker]_.
  
* The GroupInfo class should be moved into this module.

.. [#Marker] For historic reasons the ``IGSGroupFolder`` marker, which 
   is used to indicate that a group is a group, is in
   ``Products.XWFChat``. What we need to do is `move IGSGroupFolder
   <https://projects.iopen.net/groupserver/ticket/419>`_

