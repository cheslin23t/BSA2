document.getElementById("submitform").onsubmit = function() {
    document.getElementById("submitbutton").hidden = true;
    setTimeout(() => {
        document.location.href = "/";
    }, 1200);
};