

$(document).ready(function() {
    $('.small-img').click(function(e){
       $('.chat').removeAttr('hidden');
    });

    $('.chat-msg').keyup(function(e) {
        if(e.which == 13) {
            var msg = $(this).val();
            var last = $($(this).parent()).parent();
            last = last.prev();
            last = last.children().first();
            last = last.children().last();
            var new_msg = last.clone();
            var cm = new_msg.find('.msg-text');
            console.log(s=cm);
            $(cm).text(msg);
            $(new_msg).insertAfter($(last));
            $(this).val(null);
        }
    });
    console.log('send ajaxs');
    getMovies(3);
    //getPeople(3);
});
