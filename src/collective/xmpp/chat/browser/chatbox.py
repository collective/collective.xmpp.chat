from zope.interface import implements
from zope.component.hooks import getSite

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.xmpp.chat.browser.interfaces import IChatBox


class ChatBox(BrowserView):
    """ """
    implements(IChatBox)
    template = ViewPageTemplateFile('templates/chatbox.pt')

    def get_fullname(self, username):
        """ Get user via his ID and return his fullname
        """
        pm = getToolByName(self.context, 'portal_membership')
        member = pm.getMemberById(username)
        if not member:
            return username # Not sure what to do here...

        if not member.hasProperty('fullname'):
            return username
        return member.getProperty('fullname') or username

    def get_box_title(self, chat_id):
        """ """
        if not '_' in chat_id:
            return chat_id

        chat_type, jid = chat_id.split('_', 1)
        contact = jid.rsplit('@', 1)[0]
        if chat_type == 'chatbox':
            return self.get_fullname(contact)
        elif chat_type == 'chatroom':
            return getSite().unrestrictedTraverse(contact).Title()
        return contact

    def render_chat_box(self, chat_id, box_id, jid):
        """ """
        chat_type, audience = chat_id.split('_', 1)
        return self.template(
                        audience=audience,
                        jid=jid,
                        box_id=box_id, 
                        chat_type=chat_type,
                        chat_id=chat_id ,)

