document.addEventListener("DOMContentLoaded", () => {
    let button = document.getElementsByClassName("buttons")
    let body = document.querySelector("body")
    
    console.log(body);
    
    for (let i = 0 ; i < button.length ; i++) {
        button[i].addEventListener("click", function() {
            if (button[i].getAttribute("id") == "red") {
                console.log(body);
                body.style['background-color'] = "red";
            } else if (button[i].getAttribute("id") == "green") {
                body.style['background-color'] = "green";
            } else {
                body.style['background-color'] = "blue";
            }
        })
    }
    })