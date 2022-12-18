const sc= document.getElementsByClassName('multi_cards');
for(let i=0; i<sc.length; i++){
    sc[i].scrollLeft=50 ; 
}
const detail = document.getElementsByClassName('vr_detalles');
const opciDoce = document.querySelector('.oper_assero')
for (let i =0; i<detail.length; i++){
    detail[i].addEventListener("click",function(){
    opciDoce.classList.toggle('inactivo');
    });
}

const btnXdoc = document.querySelector('.elimEstu');
const btnAddoc = document.querySelector('#btAgreMod');
const btnCanceldoc =document.querySelector('#btCanMod');

const formuDelete = document.querySelector('.us_Cdelete');

//Primer Menu
const formuAdd = document.querySelector('.add_student');
btnAddoc.addEventListener("click",function(){
opciDoce.classList.toggle('inactivo');
formuAdd.classList.toggle('inactivo');
});



btnCanceldoc.addEventListener("click",function(){
    opciDoce.classList.toggle('inactivo');
});

//Segundo Menu ¿Deseas eliminar el estudiante?

btnXdoc.addEventListener("click",function(){
    opciDoce.classList.toggle('inactivo');
    formuDelete.classList.toggle('inactivo');
})




const btnAcep2M = document.querySelector('#deleteAlumno')
const msjAlumEli = document.querySelector('.us_delete ');


btnAcep2M.addEventListener("click",function(){
formuDelete.classList.toggle('inactivo');
msjAlumEli.classList.toggle('inactivo');
})
const btnCancel2M =document.querySelector('#cancelDeleteAlumno');
btnCancel2M.addEventListener("click",function(){
    opciDoce.classList.toggle('inactivo');
    formuDelete.classList.toggle('inactivo');
})

const btnAcepElimina = document.querySelector('#btnAceptElim');
btnAcepElimina.addEventListener('click',function(){
    msjAlumEli.classList.toggle('inactivo');
})


//Tercer Menu ¿Deseas Agregar un alumno?


const btnAddConfi =document.querySelector('.addEstu');
const msjAddEstu = document.querySelector('.us_Cadd');
btnAddConfi.addEventListener("click",function(){
    formuAdd.classList.toggle('inactivo');
msjAddEstu.classList.toggle('inactivo');
});
const btnCanConfi = document.querySelector('#btnCloseBusc');
btnCanConfi.addEventListener("click",function(){
    formuAdd.classList.toggle('inactivo');
    opciDoce.classList.toggle('inactivo');
    
});

//Tercer Menu botones Aceptar / Cancelar
const msjDilogAgregado = document.querySelector('.us_add');
const btnAcAdd = document.querySelector('#addAlumno');
btnAcAdd.addEventListener("click",function(){
    msjAddEstu.classList.toggle('inactivo');
msjDilogAgregado.classList.toggle('inactivo');
});
const btnCanAdd = document.querySelector('#canceladdAlumno'); 
btnCanAdd.addEventListener("click",function(){
    msjAddEstu.classList.toggle('inactivo');
    formuAdd.classList.toggle('inactivo');
});
//Tercer Menu confirmacion de agregado
const acepDialog = document.querySelector('#btnAcepAdd');
acepDialog.addEventListener("click",function(){
    msjDilogAgregado.classList.toggle('inactivo');
    formuAdd.classList.toggle('inactivo');
});