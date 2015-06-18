$("#edit").click(function () {
    $.post("/user/edit", {nickname: $("input[name='nickname']").val(), email: $("input[name='email']").val(), birth_date: $("input[name='birth_date']").val()}, function (data) {
        if (data.status == 'ok') {
            addMessage("Updating profile done successfully!", "success", "message");
            $('.nickname').text($("input[name='nickname']").val());
        }
        else {
            addMessage("Problem with updating profile!", "danger", "message");
        }
    });
});

$('a[data-toggle="tab"], button[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    if ($(e.target).attr('href') == "#edit-tab") {
        $("#changePassword").css("display", "");
        $("#editProfile").css("display", "none");
    }
    if ($(e.target).attr('href') != "#edit-tab") {
        $("#editProfile").css("display", "");
        $("#changePassword").css("display", "none");
    }
});

$("#change_password").click(function () {
    $.post("/user/change_password", {current_password: $("input[name='current_password']").val(), password: $("input[name='password']").val(), confirm: $("input[name='confirm']").val()}, function (data) {
        if (data.status == 1) {// your current password isn't correct
            addMessage("your current password isn't correct!", "danger", "password_message");
        }
        else if (data.status == 2) {// confirm doesn't match password
            addMessage("Please confirm your password correctly!", "warning", "password_message");
        }
        else if (data.status == 3) {// password changed successfully
            addMessage("Your password changed successfully", "success", "password_message");
        }
    });
});

function addMessage(text, type, panel) {
    var message = $('<div class="alert alert-' + type + ' alert-dismissible" role="alert" hidden="true"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span>&times;</span></button>' + text + '</div>').hide();
    $("#" + panel).prepend(message);
    message.fadeIn(500);

    setTimeout(function () {
        message.fadeOut(500, function () {
            message.remove();
        });
    }, 3000);
}