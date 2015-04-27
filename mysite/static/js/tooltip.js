$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});

/**
 * Created by hojjat on 1/24/15 AD.
 */
$(document).ready(function () {

    $(".my_input").on("keyup", function () {
        console.log(this.value.language);
        if (this.value.length <= 3) {
            $(this).tooltip("show");
        } else {
            $(this).tooltip("hide");
        }
    }).tooltip({
        placement: "bottom",
        trigger: "focus"
    });
    $('.edit_mine').click(function () {
        $('.my_input').removeAttr('disabled');
        $('#form_two').removeAttr('disabled');
        $('.edit').attr('disabled', true);
        $('.edit').fadeTo("fast", 0, function () {
        });
    });
});