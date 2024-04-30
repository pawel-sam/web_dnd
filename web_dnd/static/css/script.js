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

  /*  function move(direction){

    }*/

    grid.addEventListener('click', function(event) {
        const clickedSquare = event.target;
        clickedSquare.style.backgroundColor = "#0089bf";
    });

    const rows = 11;
    const cols = 25;
    let game_field = [];
    for (let i = 5; i > 5-rows; i--) {
    game_field[i] = [];

    for (let j = -12; j < cols-12; j++) {
    const square = document.createElement("div");
    square.classList.add("square");
    square.id = `${i}_${j}`
    square.textContent = `y= ${i} x= ${j}`;
    grid.appendChild(square);
    game_field[i][j] = square;
        }
    }
    game_field[0][0].style.backgroundColor = "red"

    document.addEventListener('keydown', function(event) {
    if (event.key === 'w' || event.key === 'W') {
        console.log('Клавиша "W" была нажата.');
        console.log(game_field[5][-12]);
        for (let i = 5; i > 5-rows; i--) {
            for (let j = -12; j < cols-12; j++) {
            var idParts = game_field[i][j].id.split('_');
            var y_id = parseInt(idParts[0], 10);
            var x_id = parseInt(idParts[1], 10);
            console.log(y_id, x_id);
            game_field[y_id][x_id].style.backgroundColor = "#6e2a00";
            }
        }
/*        for (let y of game_field){
            for (let x of y)
            var idParts = x.id.split('_');
            var y_id = parseInt(idParts[0], 10);
            var x_id = parseInt(idParts[1], 10);
            console.log(y_id, x_id)
        }*/
/*        for (let y of game_field) { // выводятся ячейки только с положительными значениями индексов
            for (let x of y) {}}*/

    }
});
});