var x = true;
window.onscroll = function (ev) {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight & x) {
        x = false;
        $.post("/post/get_post", {'num': 1, 'last_date': $('.post-body:last-child').attr('date_time'), 'query': $('#query').val(), 'user_id': $('#user-id').attr('user-id')}, function (data) {
            if (data.status == 'ok') {// the user comments about the post
                var posts = JSON.parse(data.posts);
                var comments = JSON.parse(data.comments);
                var len = posts.length;
                var p;
                var start = 0;
                for (var i = 0; i < len; i++) {
                    p = posts[i];
                    var c = '<div class="panel-body post-body" date_time="' + p.date_time + '">';
                    c += '<a href="/profile/' + p.username + '"><img class="img-responsive col-lg-3 pro-pic"';
                    c += 'src="' + p.avatar_url + '"></a>';
                    c += '<h5><a href="/profile/' + p.username + '">' + p.nickname + '</a><span ';
                    c += 'class="text-muted date"><span class="glyphicon glyphicon-time"';
                    c += 'aria-hidden="true"></span><a href="/post/' + p.id + '"';
                    c += 'class="text-muted">' + p.date_time + '</a></span></h5>';
                    c += '<a href="/movieprofile/' + p.movie_name + '">';
                    c += '<span tabindex="0" id="movie-info1" class="color-popover" data-toggle="popover" data-trigger="hover"';
                    c += 'data-content="' + p.description + '">' + p.movie_name + '</span>';
                    c += '<div class="col-sm-12 col-md-12"><div class="thumbnail">';
                    c += '<img src="' + p.movie_url + '" alt="' + p.movie_name + ' cover photo">';
                    c += '<div class="caption">';
                    c += '<div class="star-rating rating-xs rating-disabled"><div class="rating-container rating-gly-star" data-content="">';
                    c += '<div class="rating-stars" data-content="" style="width: 100%;"></div>';
                    c += '<input class="postRate form-control hide" value="' + p.rate + '" type="number" readonly="true" data-stars="10" min="0"';
                    c += 'max="10" step="0.2" data-size="xs"></div>';
                    c += '<div class="caption"><span class="label label-default">' + p.rate + ' Stars</span></div></div>';
                    c += '<p>' + p.text + '</p>';
                    if (p.liked) {
                        c += '<div class="hr second-color text-left"><span ';
                        c += 'class="glyphicon glyphicon-comment"></span><span p-id="' + p.id + '">' + p.comments_num + ' Comments</span><span ';
                        c += 'class="glyphicon glyphicon-star star-like"';
                        c += ' id="star-like' + p.id +'"';
                        c += 'post-id="' + p.id + '"></span><span>' + p.likes + ' Favourites</span></div>';
                    }
                    else {
                        c += '<div class="hr second-color text-left"><span ';
                        c += 'class="glyphicon glyphicon-comment"></span><span p-id="' + p.id + '">' + p.comments_num + ' Comments</span><span ';
                        c += 'class="glyphicon glyphicon-star-empty star-like"';
                        c += ' id="star-like' + p.id +'"';
                        c += 'post-id="' + p.id + '"></span><span>' + p.likes + ' Favourites</span></div>';
                    }
                    var l = p.comments_num;
                    for (var j = start; j < start + l; j++) {
                        var cm = comments[j];
                        c += '<div class="media"><div class="media-left media-top my-media">';
                        c += '<a href="/profile/' + cm.username + '">';
                        c += '<img class="media-object img-circle"';
                        c += 'src="' + cm.avatar_url + '" alt="author avatar"></a></div>';
                        c += '<div class="media-body">' + cm.text + '</div></div>';
                        c += '<div class="hr second-color small-divider text-right"><span class="glyphicon glyphicon-time" aria-hidden="true"></span>';
                        c += cm.date_time + '</div>';
                    }
                    c += '<div class="media">' + '<div class="media-left media-top my-media">';
                    c += '<a href="/profile/' + data.username + '">';
                    c += '<img class="media-object img-circle"';
                    c += 'src="' + data.avatar_url + '" alt="user avatar"></a></div>';
                    c += '<div class="media-body"><div class="input-group col-lg-12 col-xs-12">';
                    c += '<textarea type="text" class="form-control comment" id="comment-post-id';
                    c += p.id + '" post-id="' + p.id + '"placeholder="Add comment..."></textarea>';
                    c += '</div></div></div></div></div><hr class="divider"></div></div>';
                }
                console.log(c);
                $('#post-tab').append(c);
                $('.post-body:last-child .comment#comment-post-id' + p.id).keyup(function (e) {
                    e.preventDefault();
                    e.stopPropagation();
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
                $('.post-body:last-child .star-like#star-like' + p.id).click(function (e) {
                    e.preventDefault();
                    e.stopPropagation();
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
                x = true;
                $(function () {
                    $('[data-toggle="popover"]').popover()
                })
            }
        });
    }
};
