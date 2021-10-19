// Flash messages //
var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
        var div = this.parentElement;
        div.style.opacity = "0";
        setTimeout(function () { div.style.display = "none"; }, 600);
    };
}

/* Login / Registration page */
$("#signup").click(function () {
    $("#first").fadeOut("fast", function () {
        $("#second").fadeIn("fast");
    });
});

$("#signin").click(function () {
    $("#second").fadeOut("fast", function () {
        $("#first").fadeIn("fast");
    });
});

$(function () {
    const regForm = $("form[name='login']").validate({
        rules: {
            username: {
                required: true,
                username: true
            },
            password: {
                required: true,
            }
        },
        messages: {
            username: "Please enter a valid username",
            password: {
                required: "Please enter password",
            }
        },
        submitHandler: function (form) {
            form.submit();
        }
    });

    console.log(regForm) 
});

$(function () {
    $("form[name='registration']").validate({
        rules: {
            username: "required",
            lastname: "required",
            password: {
                required: true,
                minlength: 5
            }
        },

        messages: {
            username: "Please enter your username",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
        },

        submitHandler: function (form) {
            form.submit();
        }
    });
});
