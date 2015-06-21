$('.star-like').click(function (e) {
    e.preventDefault();
    var c = e.target;
    if ($(c).hasClass('glyphicon-star-empty')) {
        $.post("/post/" + $(c).attr('post-id') + "/like", {'req': 0}, function (data) {
            if (data.status == 'like') {// the user likes the post
                $(c).removeClass('glyphicon-star-empty');
                $(c).addClass('glyphicon-star');
                $($(c).next()).text(data.likes + " Favourites");
            }
        });
    }
    else if ($(c).hasClass('glyphicon-star')) {
        $.post("/post/" + $(c).attr('post-id') + "/like", {'req': 1}, function (data) {
            if (data.status == 'unlike') {// the user unlikes the post
                $(c).removeClass('glyphicon-star');
                $(c).addClass('glyphicon-star-empty');
                $($(c).next()).text(data.likes + " Favourites");
            }
        });
    }
});