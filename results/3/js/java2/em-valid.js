function validateForm() {
    var x = document.forms["mytld"]["emqll"].value;
    var atpos = x.indexOf("@");
    if (atpos< 1 || dotpos<atpos+2 || dotpos+2>=x.length) {
        alert("Please enter a valid email address");
        return false;
    }
}