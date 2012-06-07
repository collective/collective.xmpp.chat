from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class OnlineContacts(ViewletBase):
    """ This viewlet is registered for and rendered inside the IPortalFooter
        viewletmanager. 
    """
    index = ViewPageTemplateFile('templates/onlinecontacts.pt')


class ChatData(ViewletBase):
    """ """
