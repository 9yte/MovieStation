function getNotif(){
    console.log("getNotif");
    $.post("/notif", {}, function(data){
        if(data.status){
            console.log("OK!!");
            for(var i = 0; i < data.notifs.length; i++){
                var cm = JSON.parse(data.notifs[i])[0];
                var html = '<li><a href="'+ cm.fields.url + '">' + cm.fields.text+ '</a></li>';
                html = html + '<li class="divider"></li>';
                var $html = $(html);
                $('ul#notif-menu').append($html);
            }
        }
    });
}