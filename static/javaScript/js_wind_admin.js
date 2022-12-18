//Manejo de los Avisos
const btnAviso = document.querySelector('#btnAV');
const contAviso = document.querySelector('.avisos')
btnAviso.addEventListener("click",function(){
contAviso.classList.toggle('inactivo');
});

//--Aceptar el aviso
const msjAviso = document.querySelector('.avisoEnv');
const cancelAvi = document.querySelector('#canAviso');
const aceptAvi = document.querySelector("#acepAviso");
aceptAvi.addEventListener("click",function(){
    contAviso.classList.toggle('inactivo');
    msjAviso.classList.toggle('inactivo');
})
cancelAvi.addEventListener("click",function(){
contAviso.classList.toggle('inactivo');
});

//Aviso Aceptado
const btnAciAceptado = document.querySelector('#avienv');
const msjEnv = document.querySelector('.avisoEnv')
btnAciAceptado.addEventListener("click",function(){
msjEnv.classList.toggle('inactivo');
})

// Manejo de las aserorias
const btnModifi = document.querySelector("#btnNV");
const formuModifi = document.querySelector(".modificaciones");
btnModifi.addEventListener("click",function(){
formuModifi.classList.toggle("inactivo");
})

//--Cancelar Modifi
const canModi = document.querySelector('#modiCancelada');
canModi.addEventListener("click",function(){
formuModifi.classList.toggle('inactivo');
});
const AcepModi = document.querySelector('#modiAceptada');
const msjAcepModi = document.querySelector('.msjAseso');
AcepModi.addEventListener("click",function(){
formuModifi.classList.toggle('inactivo');
//msjAcepModi.classList.toggle('inactivo');
});

//Cerrar Mensaje de la asesoria guardada
const btnAcepModif= document.querySelector('#AceptF');
btnAcepModif.addEventListener("click",function(){
msjAcepModi.classList.toggle('inactivo');
});
