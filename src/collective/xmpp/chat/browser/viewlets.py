from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class OnlineContacts(ViewletBase):
    """ This viewlet is registered for and rendered inside the IPortalFooter
        viewletmanager. 
    """
    index = ViewPageTemplateFile('templates/onlinecontacts.pt')


class ChatData(ViewletBase):
    """ This is a hidden viewlet that stores the current username and 
        base url on the page.
    """

class ChatViewlet(ViewletBase):
    """ """

    def update(self):
        super(ChatViewlet, self).update()
        self.anonymous = self.portal_state.anonymous()
