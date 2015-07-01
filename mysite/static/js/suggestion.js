var busy = false
function getMovies(n) {
    console.log("getMovies");
    if($('div#movie-interest').attr('data-sugg') == 'not-set'){
        console.log('send ajaxs');
        busy = true
        $.post("/movieprofile/suggestions/" + n, {}, function(data){
            if(data.status){
                /*console.log(data.Movies.length);*/
                for(var i = 0; i < data.Movies.length; i++){
                    /*console.log(JSON.parse(data.Movies[i])[0])*/
                    var mov = JSON.parse(data.Movies[i])[0];
                    var html = '<div class="media">'+
                                '<div class="media-left media-top popular-movie">' +
                                    '<a href="/movieprofile/' + mov.fields.name + '">' +
                                        '<img class="media-object img-rounded" src="/media/'+ mov.fields.cover_photo +'">' +
                                    '</a>' +
                                '</div>' +
                                '<div class="media-body">' +
                                    '<a href="/movieprofile/'+ mov.fields.name + '" '+
                                        '<h6 class="media-heading">' + mov.fields.name + '</h6>' +
                                    '</a>' +
                                '</div>' +
                            '</div>' +
                            '<hr class="divider small-divider">';
                    var $html = $(html);
                    $('div#movie-interest').append($html);
                    $('div#movie-interest').attr('data-sugg', 'set');
                }
            }
            busy = false;
            getPeople(3);
        });
    }
}

function getPeople(n) {
    busy = true
    $.post("/profile/suggestions/" + n, {}, function(data){
        if(data.status){
            for(var i = 0; i < data.Peoples.length; i++){
                var person = JSON.parse(data.Peoples[i])[0];
                console.log(person.fields.username);
                var display_name;
                if(person.fields.first_name != "" && person.fields.first_name != " ")
                    display_name = person.fields.first_name + person.fields.last_name;
                else
                    display_name = person.fields.username

                var html = '<div class="media">' +
                                '<div class="media-left media-top popular-movie">' +
                                    '<a href="/profile/'+person.fields.username +'">' +
                                        '<img class="media-object img-rounded" src="/media/'+ person.fields.avatar +'" alt="...">' +
                                    '</a>' +
                                '</div>' +
                                '<div class="media-body">' +
                                    '<h6 class="media-heading">' + display_name + '</h6>' +
                                    '4 mutual follower' +
                                '</div>' +
                            '</div>' +
                            '<hr class="divider small-divider">';
                var $html = $(html);
                $('div#people-interest').append($html);

            }
        }
        getNotif();
        busy = false;
    });
}


