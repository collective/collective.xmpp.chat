============
Introduction
============

``collective.chat.xmpp`` provides instant messaging for Plone_. It uses the 
XMPP_ protocol and requires an XMPP server (such as ejabberd_) for the message handling.

============
Installation
============
 
XMPP integration with Plone is provided by the `collective.xmpp.core`_ package.
Please refer to its README on how to set it up.

Alternatively you can also use the buildout included in this package.

Before setting up the package you need to have a working XMPP server and access to the 
administration account on the server. 

Your XMPP server will have to support the following extensions

* `XEP-0045`_ Multi-user Chat
* `XEP-0071`_ XHTML-IM.
* `XEP-0144`_ Roster Item Exchange.
* `XEP-0124`_ Bidirectional-streams Over Synchronous HTTP (BOSH)
* `XEP-0206`_ XMPP over BOSH


.. _XEP-0045: http://xmpp.org/extensions/xep-0045.html
.. _XEP-0071: http://xmpp.org/extensions/xep-0071.html
.. _XEP-0144: http://xmpp.org/extensions/xep-0144.html
.. _XEP-0124: http://xmpp.org/extensions/xep-0124.html
.. _XEP-0206: http://xmpp.org/extensions/xep-0206.html
.. _collective.xmpp.core: http://github.com/collective/collective.xmpp.core
.. _Plone: http://plone.org
.. _XMPP: http://xmpp.org
.. _ejabberd: ejabberd.im
