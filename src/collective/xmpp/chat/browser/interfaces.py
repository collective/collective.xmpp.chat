from zope.interface import Interface

class IXMPPChatLayer(Interface):
    """Marker Interface for a custom BrowserLayer
    """

class IChatBox(Interface):
    """ """
    def render_chat_box(self, box_id, user, contact):
        """ """
