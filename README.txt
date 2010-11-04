.. sectnum::

============
Introduction
============

The code that defines the core of GroupServer groups. The main thing
that is defined is the ``GroupPage`` view. 

TODO
====

* The marker interface for groups will be moved into this module
  [#Marker]_.
  
* The GroupInfo class should be moved into this module.

.. [#Marker] For historic reasons the ``IGSGroupFolder`` marker, which 
   is used to indicate that a group is a group, is in
   ``Products.XWFChat``. What we need to do is `move IGSGroupFolder
   <https://projects.iopen.net/groupserver/ticket/419>`_

