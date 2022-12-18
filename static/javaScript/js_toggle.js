const body = document.querySelector('body');
const toggle = document.getElementById('toggle');
const tarjetas = document.querySelector('.zona_tarjetas');
const tabla = document.querySelector('.tabla_horarios');

toggle.onclick = function(){
    toggle.classList.toggle('active');
    tarjetas.classList.toggle('inactivo');
    tabla.classList.toggle('inactivo');
    console.log("Activado");
}