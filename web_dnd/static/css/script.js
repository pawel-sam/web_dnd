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
/*    function move(direction){

    }*/

    grid.addEventListener('click', function(event) {
        const clickedSquare = event.target;
        clickedSquare.style.backgroundColor = getRandomColor();
    });

    const rows = 11;
    const cols = 25;
    let game_field = [];
    for (let i = 5; i > 5-rows; i--) {
    game_field[i] = [];

    for (let j = -12; j < cols-12; j++) {
    const square = document.createElement("div");
    square.classList.add("square");
    square.textContent = `y= ${i} x= ${j}`;
    grid.appendChild(square);
    game_field[i][j] = square;
    console.log(game_field.length);
        }
    }
    game_field[0][0].style.backgroundColor = "red"
});