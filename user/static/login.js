function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


function myFunction2() {
    var x = document.getElementById("id_new_password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


function myFunction3() {
    var x = document.getElementById("id_new_password2");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function changePassword1() {
    var x = document.querySelector('input[name="old_password"]');
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function changePassword2() {
    var x = document.querySelector('input[name="new_password1"]');
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function changePassword3() {
    var x = document.querySelector('input[name="new_password2"]');
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function changePassword() {
    changePassword1();
    changePassword2();
    changePassword3();
}