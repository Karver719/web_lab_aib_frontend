document.addEventListener("DOMContentLoaded", () => {
    let redInput = document.querySelector('input[name="red"]')
    let greenInput = document.querySelector('input[name="green"]')
    let blueInput = document.querySelector('input[name="blue"]')
    let window = document.querySelector('div[name=window]')
    
    let red = redInput.value
    let green = greenInput.value
    let blue = blueInput.value
    
    redInput.oninput = function(){
        red = redInput.value
    
        window.style['background-color'] = 'rgb('+red+', '+green+', '+blue+')'
        console.log(redInput.value)
    }
    
    greenInput.oninput = function(){
        green = greenInput.value
    
        window.style['background-color'] = 'rgb('+red+', '+green+', '+blue+')'
        console.log(greenInput.value)
    }
    
    blueInput.oninput = function(){
        blue = blueInput.value
    
        window.style['background-color'] = 'rgb('+red+', '+green+', '+blue+')'
        console.log(blueInput.value)
    }
    
    })