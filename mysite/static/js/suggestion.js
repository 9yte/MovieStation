var busy = false
function getMovies(n) {
    busy = true
    $.post("movieprofile/suggestions/" + n, {}, function(data){
        if(data.status){
            console.log(data.Movies.length);
            for(var i = 0; i < data.Movies.length; i++){
                console.log(JSON.parse(data.Movies[i])[0])
                var mov = JSON.parse(data.Movies[i])[0];
                var html = '<div class="media">'+
                            '<div class="media-left media-top popular-movie">' +
                                '<a href="movieprofile/' + mov.fields.name + '">' +
                                    /*'<img class="media-object img-rounded" src="{% static  %}" alt="...">' +*/
                                    '<p>RRRR</p>' +
                                '</a>' +
                            '</div>' +
                            '<div class="media-body">' +
                                '<h6 class="media-heading">' + mov.fields.name + '</h6>' +
                                ' 4 follower favourites this movie!' +
                            '</div>' +
                        '</div>' +
                        '<hr class="divider small-divider">';
                var $html = $(html);
                $('div#movie-interest').append($html);

            }
        }
        busy = false;
    });
}

$(document).ready(function(){
    console.log('send ajaxs');
    getMovies(3);
});


