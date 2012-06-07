from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from babble.ui.browser.interfaces import IChatBox
from babble.ui.browser import chatbox

class ChatBox(chatbox.ChatBox):
    """ """
    implements(IChatBox)
    template = ViewPageTemplateFile('templates/chatbox.pt')

    def render_chat_box(self, chat_id, box_id, tzoffset, jid):
        """ """
        chat_type, audience = chat_id.split('_', 1)
        # response = utils.get_last_conversation(
        #                                 self.context, 
        #                                 audience, 
        #                                 chat_type)
        # if response['status'] != config.SUCCESS:
        #     raise NotFound
        # if chat_type == 'chatroom':
        #     messages = response['chatroom_messages']
        # else:
        #     messages = response['messages']

        # TODO:
        # 
        # We should here query for a utility. That utility is then implemented
        # in either babbble.client or babble.xmpp
        messages = {}

        messages = self._to_local_timezone(messages, tzoffset)
        return self.template(
                        messages=messages, 
                        audience=audience,
                        jid=jid,
                        box_id=box_id, 
                        chat_type=chat_type,
                        chat_id=chat_id ,)

