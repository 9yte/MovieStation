$("#edit").click(function () {
    $target = $(this);

    $.post("/user/edit", {nickname: $("input[name='nickname']").val(), email: $("input[name='email']").val(), birth_date: $("input[name='birth_date']").val()}, function (data) {
        if (data.status == 'ok') {
            addMessage("Updating profile done successfully!", "success");
            $('.nickname').text($("input[name='nickname']").val());
        }
        else {
            addMessage("Problem with updating profile!", "danger");
        }
    });
});

function addMessage(text, type) {
    var message = $('<div class="alert alert-' + type + ' alert-dismissible" role="alert" hidden="true"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span>&times;</span></button>' + text + '</div>').hide();
    $("#message").prepend(message);
    message.fadeIn(500);

    setTimeout(function () {
        message.fadeOut(500, function () {
            message.remove();
        });
    }, 3000);
}