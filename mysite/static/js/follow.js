$(".follow").click(function(){
    $target = $(this);
    $.post("/user/" + $target.attr('data-follow'), {followed : this.id}, function(data){
        if(data.status == 'ok'){
            if($target.attr('data-follow') == 'follow'){
                $target.attr('data-follow', 'unfollow');
                $target.text('unfollow');
            }
            else{
                $target.attr('data-follow', 'follow')
                $target.text('follow');
            }
        }
    });
});