from Products.CMFCore.utils import getToolByName

def updateJSRegistry(context):
    js_registry = getToolByName(context, 'portal_javascripts')
    for rid in ["++resource++collective.xmpp.chat.javascripts/underscore.js",
                "++resource++collective.xmpp.chat.javascripts/underscore.string/lib/underscore.string.js",
                "++resource++collective.xmpp.chat.javascripts/backbone.js",
                "++resource++collective.xmpp.chat.javascripts/burry.js/burry.js",
                "++resource++collective.xmpp.chat.javascripts/sjcl/sjcl.js",
                "++resource++collective.xmpp.chat.javascripts/strophe.roster.js",
                "++resource++collective.xmpp.chat.javascripts/strophe.muc.js",
                "++resource++collective.xmpp.chat.javascripts/converse.js"]:
        js_registry.unregisterResource(rid)
    context.runImportStepFromProfile('profile-collective.xmpp.chat:default', 'jsregistry')


def updateCSSRegistry(context):
    css_registry = getToolByName(context, 'portal_css')
    for rid in ["++resource++collective.xmpp.chat.stylesheets/main.js"]:
        css_registry.unregisterResource(rid)
    context.runImportStepFromProfile('profile-collective.xmpp.chat:default', 'cssregistry')


