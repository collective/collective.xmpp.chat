from zope.i18nmessageid import MessageFactory

messageFactory = MessageFactory('collective.xmpp.chat')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
