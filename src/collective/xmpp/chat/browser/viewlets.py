from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from jarn.xmpp.core.browser.viewlet import XMPPViewlet

class OnlineContacts(ViewletBase):
    """ This viewlet is registered for and rendered inside the IPortalFooter
        viewletmanager. 
    """
    index = ViewPageTemplateFile('templates/onlinecontacts.pt')


class ChatData(ViewletBase):
    """ This is a hidden viewlet that stores the current username and 
        base url on the page.
    """

class ChatViewlet(XMPPViewlet):
    """ """
