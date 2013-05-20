$('#chatpanel').ready(function () {
    converse.initialize({
        animate: true,
        prebind: true,
        xhr_user_search: true,
        auto_subscribe: $('collective-xmpp-chat-data').attr('auto_subscribe'),
        auto_list_rooms: false
    });
});

$(document).on('jarnxmpp.connected', function (ev, connection) {
    converse.onConnected(connection);
});
