let password = ()=>{
    PasswordLength = document.getElementById("PasswordLength").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "password?PasswordLength"+"="+PasswordLength, true);
    xhttp.send();
}
