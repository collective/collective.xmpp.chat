from zope.interface import implements
from zope.component.hooks import getSite

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.xmpp.chat.browser.interfaces import IChatBox
from collective.xmpp.chat import iso8601


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

        chat_type, contact = chat_id.split('_', 1)
        if chat_type == 'chatbox':
            return self.get_fullname(contact)
        elif chat_type == 'chatroom':
            return getSite().unrestrictedTraverse(contact).Title()
        return contact

    def _to_local_timezone(self, messages, tzoffset):
        tzoffset = iso8601.FixedOffset(0, int(tzoffset), '')
        for key in messages.keys():
            for mtuple in messages[key]:
                # Change message times to local timezone
                olddate = iso8601.parse_date(mtuple[2])
                date = (olddate + tzoffset.offset).replace(tzinfo=tzoffset)
                mtuple[2] = date.isoformat()
        return messages

    def render_chat_box(self, chat_id, box_id, tzoffset, jid):
        """ """
        chat_type, audience = chat_id.split('_', 1)
        # TODO: Get message history
        messages = {}
        messages = self._to_local_timezone(messages, tzoffset)
        return self.template(
                        messages=messages, 
                        audience=audience,
                        jid=jid,
                        box_id=box_id, 
                        chat_type=chat_type,
                        chat_id=chat_id ,)
