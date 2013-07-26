from collective.xmpp.core.interfaces import IProductLayer
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.testing import z2
from zope.configuration import xmlconfig
from zope.interface import alsoProvides


class XMPPChatFixture(PloneSandboxLayer):
    """ """

    def setUpZope(self, app, configurationContext):
        import collective.xmpp.chat
        import Products.UserAndGroupSelectionWidget
        xmlconfig.file('configure.zcml', Products.UserAndGroupSelectionWidget,
                       context=configurationContext)
        xmlconfig.file('configure.zcml', collective.xmpp.chat,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.xmpp.chat:default')
        # Manually enable the xmpp.core browserlayer
        alsoProvides(portal.REQUEST, IProductLayer)


XMPPCHAT_FIXTURE = XMPPChatFixture()

XMPPCHAT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(XMPPCHAT_FIXTURE, z2.ZSERVER_FIXTURE),
    name="collective.xmpp.chatLayer:Functional"
)
