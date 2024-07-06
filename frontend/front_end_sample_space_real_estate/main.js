checkPasswordLength = false;
checkPasswordConfirm = false;

$(document).ready(function() {
    // PASSWORD CORRECT
    $("#recipient-password").on('keypress', function (event) {
        const keyName = document.getElementById("recipient-password").value + event.key;
        const keyName2 = document.getElementById("recipient-password-verify").value;
        if (keyName != keyName2) {
            $("#recipient-password-verify").addClass("is-invalid");
            $("#recipient-password-verify").removeClass("is-valid");
        } else {
            $("#recipient-password-verify").addClass("is-valid");
            $("#recipient-password-verify").removeClass("is-invalid");
        }
    });

    // PASSWORD2 CORRECT
    $("#recipient-password-verify").on('keypress', function (event) {
        const keyName = document.getElementById("recipient-password").value;
        const keyName2 = document.getElementById("recipient-password-verify").value + event.key;
        if (keyName != keyName2) {
            $("#recipient-password-verify").addClass("is-invalid");
            $("#recipient-password-verify").removeClass("is-valid");
        } else {
            $("#recipient-password-verify").addClass("is-valid");
            $("#recipient-password-verify").removeClass("is-invalid");
        }
    });

    // LOGIN ACTION
    $("#login-button").on('click', function(event) {
        alert("logging in");
    });

    // SIGNUP ACTION
    $("#signup-button").on('click', function(event) {
        alert("signing in");
    });

    // CHANGE NAVBAR ITEM COLOR ONCLICK
    $(".").on('click', function(event) {

    });
});