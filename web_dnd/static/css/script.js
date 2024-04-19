document.addEventListener("DOMContentLoaded", function() {
  const grid = document.querySelector('.grid');

  function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  for (let i = 0; i < 275; i++) {
    const square = document.createElement("div");
    square.classList.add("square");
//    square.style.backgroundColor = getRandomColor(); // Применяем цвет из массива colors
    grid.appendChild(square);
  }

  grid.addEventListener('click', function(event) {
    const clickedSquare = event.target;
    clickedSquare.style.backgroundColor = getRandomColor();
  });
});