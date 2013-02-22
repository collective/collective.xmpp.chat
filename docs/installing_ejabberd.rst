Installing and configuring ejabberd:
====================================

In order to user collective.xmpp.chat you'll need a working XMPP server that supports the following extensions:

* `XEP-0049`_ Private XML Storage
* `XEP-0054`_ vCard-temp.
* `XEP-0071`_ XHTML-IM.
* `XEP-0124`_ Bidirectional-streams Over Synchronous HTTP (BOSH)
* `XEP-0133`_ Service Administration.
* `XEP-0136`_ Server side archiving of messages
* `XEP-0144`_ Roster Item Exchange.
* `XEP-0206`_ XMPP over BOSH

.. _enable-mysql-support-for-ejabberd:

MySQL support for ejabberd
--------------------------

MySQL support for ejabberd is provided via an addon module.

Quick  instructions:

1. svn checkout http://svn.process-one.net/ejabberd-modules/mysql/trunk/ mysql
2. ./build.sh
3. Copy the beam files
4. Start ejabberd again

.. _enable-mod_archive-support-for-ejabberd:

Installing mod_archive for server side message storing
------------------------------------------------------

To enable server side archiving of chat messages (required for later retrievel,
such as on a page reload), we need to install the mod_archive_ (implementing XEP-0136_)
add-on module for ejabberd.

1. Additional modules for ejabberd are stored in the ejabberd-modules_ svn repository. ::

    svn co https://svn.process-one.net/ejabberd-modules

   Note: If you are using a source checkout of collective.xmpp.chat, you can use
   mr.developer_ to check it out for you::

    ./bin/develop checkout ejabberd-modules

2. Now navigate to the directory of the mod_archive module. If you used mr.developer, it will be in the *src* directory inside your buildout directory::

    cd ./src/ejabberd-modules/mod_archive/trunk/

3. Now compile the module:

   - On GNU/Linux, \*BSD, etc.::
       ./build.sh

   - On Windows:::
       build.bat

   - If you use an ejabberd binary installer, place the module source file in bin/ and run:::
       erlc -I includes/ejabberd/include mod_archive.erl

4. Now copy the generated *.beam* files from the *ebin* directory to where youre ejabberd *.beam* files are.
   For example, if you are using the supplied *buildout.cfg* file:::

    cp ./src/ejabberd-modules/mod_archive/trunk/ebin/mod_archive_odbc.beam ./parts/ejabberd/lib/ejabberd/ebin/
    cp ./src/ejabberd-modules/mod_archive/trunk/ebin/mod_archive_webview.beam ./parts/ejabberd/lib/ejabberd/ebin/

5. Edit *ejabberd.cfg* and add the HTTP and module definitions {["archive"], mod_archive_webview} to
   the list of request handlers: ::
        listen, [
            {5280, ejabberd_http, [
                {
                    request_handlers, [{["archive"], mod_archive_webview}]
                }
            ]}
        ]

6. Now start ejabberd. If there's a problem, probably ejabberd log files will report an error message.


.. _XEP-0049: http://xmpp.org/extensions/xep-0049.html
.. _XEP-0054: http://xmpp.org/extensions/xep-0054.html
.. _XEP-0060: http://xmpp.org/extensions/xep-0060.html
.. _XEP-0071: http://xmpp.org/extensions/xep-0071.html
.. _XEP-0124: http://xmpp.org/extensions/xep-0124.html
.. _XEP-0133: http://xmpp.org/extensions/xep-0133.html
.. _XEP-0136: http://xmpp.org/extensions/xep-0136.html
.. _XEP-0144: http://xmpp.org/extensions/xep-0144.html
.. _XEP-0206: http://xmpp.org/extensions/xep-0206.html
.. _XEP-0248: http://xmpp.org/extensions/xep-0248.html
.. _ejabberd-modules: http://svn.process-one.net/ejabberd-modules/
.. _mod_archive: http://www.ejabberd.im/mod_archive
.. _mr.developer: http://pypi.python.org/pypi/mr.developer
