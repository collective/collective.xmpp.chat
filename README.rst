Introduction
============

``collective.chat.xmpp`` provides instant messaging for `Plone`_.

It provides a web-based chat client, by means of `Converse.js`_, a javascript
library which makes use of the open and very popular `XMPP`_  messaging protocol.

You will need an XMPP server (such as `ejabberd`_) for the message handling.

Features
========

* Manually or automatically subscribe to other users.
* With manual roster subscriptions, you can accept or decline contact requests.
* Chat statuses (online, busy, away, offline)
* Custom status messages
* Typing notifications (i.e when the contact is typing)
* Third person messages (/me )
* Multi-user chat in chatrooms
* Chatrooms can be configured (privacy, persistency etc.)
* Topics can be set for chatrooms
* Full name and profile picture support (via VCards)

Installation
============

XMPP integration with Plone is provided by the `collective.xmpp.core`_ package.
Please refer to its README on how to set it up.

You can use the buildout at `collective.xmpp.buildout`_.

The buildout in this egg is used for development purposes.

You'll need to have a working XMPP server and access to the
administration account on the server.

Your XMPP server will have to support the following extensions

* `XEP-0045`_ Multi-user Chat
* `XEP-0071`_ XHTML-IM.
* `XEP-0144`_ Roster Item Exchange.
* `XEP-0124`_ Bidirectional-streams Over Synchronous HTTP (BOSH)
* `XEP-0206`_ XMPP over BOSH

Configuration
=============

You'll need to have an administrator account on the Jabber server you'll be
using. Refer to the `collective.xmpp.core`_ README for information on how to
set this up.

Once you've installed ``collective.xmpp.chat``, you should go to the Plone
registry in the control panel and set the ``XMPP Domain`` as well as the ``XMPP
Admin JID`` and ``XMPP Admin Password`` values.

Additionally you have the option ``Auto-subscribe XMPP users``, which is
disabled by default.

Enable this option if you don't want your users to manually maintain their
rosters (i.e subscribing and unsubscribing to one another) and would rather
have everyone subscribe to everyone else. Be careful however, this might cause
a lot of overhead (and therefore be quite slow) on sites with large userbases.


.. _`XEP-0045`: http://xmpp.org/extensions/xep-0045.html
.. _`XEP-0071`: http://xmpp.org/extensions/xep-0071.html
.. _`XEP-0144`: http://xmpp.org/extensions/xep-0144.html
.. _`XEP-0124`: http://xmpp.org/extensions/xep-0124.html
.. _`XEP-0206`: http://xmpp.org/extensions/xep-0206.html
.. _`collective.xmpp.core`: http://github.com/collective/collective.xmpp.core
.. _`collective.xmpp.buildout`: http://github.com/collective/collective.xmpp.buildout
.. _`Plone`: http://plone.org
.. _`XMPP`: http://xmpp.org
.. _`ejabberd`: http://ejabberd.im
.. _`Converse.js`: http://conversejs.org 


