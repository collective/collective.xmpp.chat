$(document).ready(function () {
    $.hook('show');
    chat_id = 'online-users-container';
    $("div#"+chat_id)
        .bind('onbeforeshow', function (e) { })
        .bind('onshow', function (e) { })
        .bind('onaftershow', function (e) { 
            var cookie = jQuery.cookie('chats-open-'+username);
            if (cookie) {
                open_chats = cookie.split('|');
            }
            if (!(chat_id in oc(open_chats))) {
                // Update the cookie if this new chat is not yet in it.
                open_chats.push(chat_id);
                var new_cookie = open_chats.join('|');
                jQuery.cookie('chats-open-'+username, new_cookie, {path: '/'});
                console.log('createChat: updated cookie = ' + new_cookie + '\n');
            }
            chats.push(chat_id);
        })
        .bind('onafterhide', function (e) { 
            var cookie = jQuery.cookie('chats-open-'+username);
            if (cookie) {
                open_chats = cookie.split('|');
            }
            new_chats = [];
            for (var i=0; i < open_chats.length; i++) {
                if (open_chats[i] != chat_id) {
                    new_chats.push(open_chats[i]);
                }
            }
            if (new_chats.length) {
                jQuery.cookie('chats-open-'+username, new_chats.join('|'), {path: '/'});
            }
            else {
                jQuery.cookie('chats-open-'+username, null, {path: '/'});
            }
        });


    $('a.user-details-toggle').live('click', function (e) {
        var userid = $(this).parent().attr('data-userid');
        startChat('chatbox_'+userid);
        e.preventDefault();
    });
});
