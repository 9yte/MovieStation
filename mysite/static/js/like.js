/**
 * Created by hojjat on 4/28/15 AD.
 */
$(document).ready(function() {
    $('.glyphicon-star-empty').click(function(e) {
        var e = $('.glyphicon-star-empty');
        $(e).removeClass('glyphicon-star-empty');
        $(e).addClass('glyphicon-star');
        alert("hi");
    });
    $('.glyphicon-star').click(function(e) {
        var e = $('.glyphicon-star');
        $(e).removeClass('glyphicon-star');
        $(e).addClass('glyphicon-star-empty');
    });
});