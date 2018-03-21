require(['converse'], function () {
    var chatdata = document.getElementById('collective-xmpp-chat-data');
    converse.initialize({
        xhr_user_search: true,
        locales_url: '++plone++collective.xmpp.chat/locale/{{{locale}}}/LC_MESSAGES/converse.json',
        auto_subscribe: chatdata.getAttribute('auto_subscribe') === "True",
        bosh_service_url: chatdata.getAttribute('bosh_url'),
        auto_list_rooms: true,
        hide_muc_server: true,
        i18n: chatdata.getAttribute('lang')||'en',
        debug: chatdata.getAttribute('debug') === "True"
    });
});
