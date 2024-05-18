document.addEventListener("DOMContentLoaded", function() {

    const rows = 28;
    const cols = 48;

    const grid = document.querySelector('.grid');
    grid.style.gridTemplateColumns = `repeat(${cols}, 50px)`
    grid.style.gridTemplateRows = `repeat(${rows}, 50px)`

    let game_field = [];

    for (let i = rows / 2; i > rows / 2 - rows; i--) {
        game_field[i] = [];
        for (let j = -1 * cols / 2; j < cols - cols / 2; j++) {
            const square = document.createElement("div");
            square.classList.add("square");
            square.id = `${i}_${j}`
            square.textContent = `y=${i} x=${j}`;
            grid.appendChild(square);
            game_field[i][j] = square;
        }
    }

    game_field[0][0].style.backgroundColor = "#ff0000";

    grid.addEventListener('click', function(event) {
        const clickedSquare = event.target;
        clickedSquare.style.backgroundColor = "#0089bf";
    });

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

//    function btn_check(){
//        {% create_map %};
//        alert("Check correct");
//    }

    document.addEventListener('keydown', function(event) {
        if (event.key === 'w' || event.key === 'W') {
            console.log('Клавиша "W" была нажата.');
            console.log(game_field[5][-12]);
            for (let i = 5; i > 5 - rows; i--) {
                for (let j = -12; j < cols - 12; j++) {
                    var idParts = game_field[i][j].id.split('_'); /*1_1_0_11, 1 = + ||| 0 = - */
                    var y_id = parseInt(idParts[0], 10);
                    var x_id = parseInt(idParts[1], 10);
                    console.log(y_id, x_id);
                    game_field[y_id][x_id].style.backgroundColor = "#6e2a00";
                }
            }


            /*   function createMap() {
               map_h, map_w = 100, 80
               map_padding = 0.1 // процент отступа от крайних значений карты
               map_h_high, map_w_high = map_h * map_padding, map_w * map_padding */
            /*формула для нахождения верхих координат*/
            /*
               map_h_low, map_w_low = map_h - map_h_high, map_w - map_w_high */
            /*формула для нахождения нижних координат*/
            /*
             */
            /* переменная процента суши, не менее 80% + суша прилегает к суше */
            /*
            //        l, s, b, m = "land", "sea", "building", "map"
                    l, s, b, m = 'l', 's', 'b', 'm'
                    map = {
                     {1:[b, y, x, [h, w]],
            //         ...
                     2000000:[m, y, x, l],
                     }
                    }
               }*/

            /*def create home(y, x, h, w) (координаты(y, x), высота, ширина)*/
            /*
            mongoDB + Django сравнение
            хранение данных
            json
            png –> svg
            svg прицеплять к div через псевдоэлемент
            */



            /* for (let y of game_field){
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