from Products.Five.browser import BrowserView
from plone.registry.interfaces import IRegistry
from collective.xmpp.chat import messageFactory as _
from collective.xmpp.core import interfaces
from collective.xmpp.core.browser import controlpanel
from zope import component
from zope import schema


class IXMPPChatSettings(interfaces.IXMPPSettings):
    """ Global XMPP settings. This describes records stored in the
        configuration registry and obtainable via plone.registry.
    """

    allow_otr = schema.Bool(
        title=_(u"label_xmpp_allow_otr",
                default=u"Allow Off-the-record encrypted chats"),
        description=_(
            u"help_xmpp_allow_otr",
            default=u"This will allow chat users to initiate OTR encrypted "
                    u"chat sessions"),
        default=False,
    )
     

class XMPPChatSettingsEditForm(controlpanel.XMPPSettingsEditForm):
    schema = IXMPPChatSettings


class XMPPChatSettingsControlPanel(controlpanel.XMPPSettingsControlPanel):
    """ XMPP settings control panel.
    """
    form = XMPPChatSettingsEditForm


class XMPPSettingsView(BrowserView):
    """ This view is used to check Registry settings
    """

    def otr_allowed(self):
        """ """
        registry = component.getUtility(IRegistry)
        settings = registry.forInterface(IXMPPChatSettings, check=False)
        return settings.allow_otr
