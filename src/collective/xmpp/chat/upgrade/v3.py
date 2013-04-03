from Products.CMFCore.utils import getToolByName


def updateJSRegistry(context):
    js_registry = getToolByName(context, 'portal_javascripts')
    for rid in [
        "++resource++collective.xmpp.chat.resources/underscore.string/lib/" \
        "underscore.string.js",
    ]:
        js_registry.unregisterResource(rid)
    context.runImportStepFromProfile('profile-collective.xmpp.chat:default',
                                     'jsregistry')
