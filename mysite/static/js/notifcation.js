function getNotif(){
    console.log("getNotif");
    $.post("/post/get_notif/", {}, function(data){
        if(data.status){
            console.log("OK!!");
            for(var i = 0; i < data.notif_comments.length; i++){
                var cm = JSON.parse(data.notif_comments[i])[0];
                var cm_owner = JSON.parse(data.cm_owners[i])[0];
                /*console.log(cm);
                console.log(cm_owner);*/
                var html = '<li><a href="/post/'+ cm.fields.post + '">' + cm_owner.fields.username + ' Commented your post</a></li>';
                html = html + '<li class="divider"></li>';
                var $html = $(html);
                $('ul#notif-menu').append($html);
            }
            for(var i = 0; i < data.notif_likes.length; i++){
                var cm = JSON.parse(data.notif_likes[i])[0];
                var cm_owner = JSON.parse(data.like_owners[i])[0];
                /*console.log(cm);
                console.log(cm_owner);*/
                var html = '<li><a href="/post/'+ cm.fields.post + '">' + cm_owner.fields.username + ' Liked your post</a></li>';
                html = html + '<li class="divider"></li>';
                var $html = $(html);
                $('ul#notif-menu').append($html);
            }
        }
    });
}