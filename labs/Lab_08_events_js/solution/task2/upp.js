const redInput = document.getElementById('redInput');
const greenInput = document.getElementById('greenInput');
const blueInput = document.getElementById('blueInput');
const colorResult = document.getElementById('colorResult');
const colorSquare = document.getElementById('colorSquare');

function changeBackgroundColor() 
{
    const red = redInput.value || 0;
    const green = greenInput.value || 0;
    const blue = blueInput.value || 0;

    if (red >= 0 && red <= 255 && green >= 0 && green <= 255 && blue >= 0 && blue <= 255) 
    {
        const rgbColor = `rgb(${red}, ${green}, ${blue})`;
        colorResult.textContent = `Выбранный цвет: ${rgbColor}`;
        colorSquare.style.backgroundColor = rgbColor;
    } else 
    {
        colorResult.textContent = 'Неверное значение';
        colorSquare.style.backgroundColor = 'white';
    }
}

redInput.addEventListener('input', changeBackgroundColor);
greenInput.addEventListener('input', changeBackgroundColor);
blueInput.addEventListener('input', changeBackgroundColor);

changeBackgroundColor();