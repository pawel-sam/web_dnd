document.addEventListener("DOMContentLoaded", function() {
    const circle = document.getElementById("circle");
    let x = 0;
    let y = 0;
    const step = 10;
  
    function moveCircle(dx, dy) {
      x += dx;
      y += dy;
      circle.style.left = x + "px";
      circle.style.top = y + "px";
    }
  
    document.addEventListener("keydown", function(event) {
      switch(event.key) {
        case "ArrowUp":
          moveCircle(0, -step);
          break;
        case "ArrowDown":
          moveCircle(0, step);
          break;
        case "ArrowLeft":
          moveCircle(-step, 0);
          break;
        case "ArrowRight":
          moveCircle(step, 0);
          break;
      }
    });
  });