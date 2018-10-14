function validateForm(){
    var pass1 = document.forms["usr_registration"]["pass1"].value;
    var pass2 = document.forms["usr_registration"]["pass2"].value;
    var username = document.forms["usr_registration"]["username"].value;
    var email = document.forms["usr_registration"]["email"].value;
    if ( email == ""){
        alert("Email can't be empty!")
        return false;
    }
    if (pass1 == ""){   
        alert("Password can't be empty!")
    }
    if (pass1 != pass2){
        alert("Password doesn't match!");
        return false;
    }
    if (username == "") {
        alert("Username can't be empty!");
        return false;
    }
    return true;
}