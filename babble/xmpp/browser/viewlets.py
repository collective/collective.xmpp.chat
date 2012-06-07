from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from jarn.xmpp.core.browser.viewlet import XMPPViewlet
from actionbar.panel.browser.viewlets import ActionViewlet

class OnlineContacts(ViewletBase):
    """ This viewlet is registered for and rendered inside the IPortalFooter
        viewletmanager. 
    """
    index = ViewPageTemplateFile('templates/onlinecontacts.pt')


class ChatData(ViewletBase):
    """ """

class ChatViewlet(XMPPViewlet, ActionViewlet):
    """ """
