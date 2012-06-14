Documentation for collective.xmpp.chat
======================================

.. toctree::
   :maxdepth: 2

**collective.chat.xmpp provides** instant messaging for Plone_. It uses an 
XMPP_ backend (via jarn.xmpp.core_) and a chat UI similar to babble.client_'s.

This is still an experimental package with development starting at the 2011
Plone Conference's sprint.

Email me for more info: jc@opkode.com

Installing mod_archive for server side message storing:
--------------------------------------------------------

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
5. Check *README.txt* or use the configuration file example provided in the conf dir to update your ejabberd.cfg configuration file.
6. Now start ejabberd. If there's a problem, probably ejabberd log files will report an error message.

.. _Plone: http://plone.org
.. _XMPP: http://xmpp.org
.. _jarn.xmpp.core: https://github.com/ggozad/jarn.xmpp.core
.. _babble.client: http://plone.org/products/babble.client
.. _mod_archive: http://www.ejabberd.im/mod_archive
.. _XEP-0136: http://www.ejabberd.im/mod_archive
.. _ejabberd-modules: http://svn.process-one.net/ejabberd-modules/
.. _mr.developer: http://pypi.python.org/pypi/mr.developer


