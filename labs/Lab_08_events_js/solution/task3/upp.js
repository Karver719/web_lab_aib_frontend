document.addEventListener("DOMContentLoaded", () => {
    let redInput = document.querySelector('input[name="red"]')
    let greenInput = document.querySelector('input[name="green"]')
    let blueInput = document.querySelector('input[name="blue"]')
    let window = document.querySelector('div[name=window]')
    
    let red = redInput.value
    let green = greenInput.value
    let blue = blueInput.value

    let colorCounter = 0
    const colorStorageCapacity = 15
    let colorStorage = document.querySelector('div[name=colorStorage]')
    let genButton = document.querySelector('input[name=generate]')
    console.log(colorStorage)
    
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

    genButton.addEventListener('click', function(){
        colorCounter += 1

        if (colorCounter == colorStorageCapacity){
            colorCounter = 0
        }

        if (colorStorage.childNodes.length < colorStorageCapacity){
            let colorStorageUnit = document.createElement('div')
            colorStorageUnit.className = 'colorStorageUnit'
            //colorStorageUnit.style['height'] = '250px'
            //colorStorageUnit.style['margin-left'] = '5px'
            colorStorageUnit.style['background-color'] = 'rgb('+red+', '+green+', '+blue+')'
            //colorStorageUnit.style['transition'] = 'height 1s'
            //colorStorageUnit.style['div:hover'] = '270px'
            colorStorage.append(colorStorageUnit)
        } else {
            colorStorage.childNodes[colorCounter].style['background-color'] = 'rgb('+red+', '+green+', '+blue+')'
        }
        
    })
})