/**
 * Created by hojjat on 4/28/15 AD.
 */
$(document).ready(function () {
    $('.comment').keyup(function (e) {
        if (e.which == 13) {
            var x = e.target;
            var comment = $(this).val();
            var p_id = $(x).attr('post-id');
            $.post("/post/" + p_id + "/comment", {'text': comment}, function (data) {
                if (data.status == 'ok') {// the user comments about the post
                    var cm = JSON.parse(data.comment)[0];
                    var c = '<div class="media"><div class="media-left media-top my-media"><a href="/profile/';
                    c += (cm.username + '">');
                    c += '<img class="media-object img-circle"src="';
                    c += cm.avatar_url;
                    c += '" alt="author avatar"></a></div>';
                    c += '<div class="media-body">';
                    c += cm.text;
                    c += '</div></div><div class="hr second-color small-divider text-right"><spanclass="glyphicon glyphicon-time" aria-hidden="true">';
                    c += '</span><ahref="/post"> ';
                    c += cm.date_time;
                    c += '</a></div>';
                    var parent = $($($(x).parent()).parent()).parent();
                    $(parent).before(c);
                    $(x).val(null);
                    $("span[p-id=" + p_id + "]").text(data.comments_num + " Comments");
                }
            });
        }
    });
});


//var comment = $(this).val();
//            var last = $($($(this).parent()).parent()).parent();
//            var last_comment = last.prev().prev();
//            var new_comment = last_comment.clone();
//            var cm = new_comment.children('.media-body');
//            $(cm).text(comment);
//            var hr = last.prev().clone();
//            var last_hr = $(last.prev());
//            $(new_comment).insertAfter($(last_hr));
//            $(hr).insertAfter($(new_comment));
//            $(this).val(null);