$(document).ready(function () {
    $('.comment').keyup(function (e) {
        e.preventDefault();
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