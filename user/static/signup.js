function myFunction() {
    var x = document.querySelector('[name="password1"]');
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function myFunction2() {
    var x = document.querySelector('[name="password2"]');
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}