$('#conversejs').ready(function () {
    $(document).unbind('jarnxmpp.connected');
    $(document).bind('jarnxmpp.connected', function (ev, connection) {
        converse.initialize({
            animate: true,
            prebind: true,
            cache_otr_key: true,
            connection: connection,
            xhr_user_search: true,
            auto_subscribe: $(this).data('autosubscribe'),
            auto_list_rooms: true,
            hide_muc_server: true,
            i18n: window.locales[$(this).data('lang')||'en'],
            debug: true
        });
    });
});
