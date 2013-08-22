$('#chatpanel').ready(function () {
    $(document).unbind('jarnxmpp.connected');
    $(document).bind('jarnxmpp.connected', function (ev, connection) {
        var $chatdata = $('#collective-xmpp-chat-data');
        converse.initialize({
            animate: true,
            prebind: true,
            connection: connection,
            xhr_user_search: true,
            auto_subscribe: $chatdata.attr('auto_subscribe'),
            auto_list_rooms: true,
            hide_muc_server: true,
            i18n: window.locales[$chatdata.attr('lang')||'en'],
            debug: true
        });
    });
});
