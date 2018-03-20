require(['converse'], function () {
    debugger;
    var chatdata = document.getElementById('collective-xmpp-chat-data');
    converse.initialize({
        xhr_user_search: true,
        auto_subscribe: chatdata.getAttribute('auto_subscribe'),
        auto_list_rooms: true,
        hide_muc_server: true,
        i18n: window.locales[chatdata.getAttribute('lang')||'en'],
        debug: true
    });
});
