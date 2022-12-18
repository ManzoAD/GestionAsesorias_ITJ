const sc= document.getElementsByClassName('multi_cards');
for(let i=0; i<sc.length; i++){
    sc[i].scrollLeft=50 ; 
}
//Apuntadores
const Inscripcion = document.querySelector("#inscribirme");
const detail = document.getElementsByClassName('vr_detalles');
const modifAsesoria = document.querySelector('.show_student');
const verProg = document.getElementsByClassName('vr_program');
const btnAcepmodif = document.querySelector('#btAgreMod');
const btnCancelmodif = document.querySelector('#btCanMod');
const winAdd = document.querySelector('.add_student');
const winAddCerrar = document.querySelector('#btnCloseBusc');

const confiInscri = document.querySelector('.btnInscrib');
const cerrar_confiInscri = document.querySelector('.btnEstadist');
const dialogInscrip = document.querySelector('.msj_confirm_inscript');

cerrar_confiInscri.addEventListener("click",function(){
Inscripcion.classList.toggle('inactivo');
});

confiInscri.addEventListener("click",function(){
    Inscripcion.classList.toggle('inactivo');
    dialogInscrip.classList.toggle('inactivo');
});

const opciAdd = document.querySelector('.addEstu');
const opciElim = document.querySelector('.elimEstu');

const diagOpciAdd = document.querySelector('.us_Cadd');
const diagOpciElim = document.querySelector('.us_Cdelete')

const confdiagOpciAdd = document.querySelector('.us_add');
const confdiagOpciElim = document.querySelector('.us_delete');

const operAdd = document.querySelector('#addAlumno');
const canOperAdd = document.querySelector("#canceladdAlumno");

const operDelete = document.querySelector('#deleteAlumno');
const canOperDelete = document.querySelector('#cancelDeleteAlumno');

const msjAgregado = document.querySelector('#btnAcepAdd');
const msjEliminado = document.querySelector('#btnAceptElim');

const btnShowClose = document.querySelector('#btnShowC');
//Eventos
for(let i=0; i<verProg.length; i++){
    verProg[i].addEventListener("click",function(){
        Inscripcion.classList.toggle('inactivo');
    })
}
for (let i =0; i<detail.length; i++)
detail[i].addEventListener("click",function(){
    modifAsesoria.classList.toggle('inactivo'); 
    console.log(i);
});
/* btnAcepmodif.addEventListener("click",WinDetalle_Open_Add); */
/* btnCancelmodif.addEventListener("click",WinDetalle_Cancel); */
winAddCerrar.addEventListener("click",closeWinAdd);

opciAdd.addEventListener("click",dialogoAgregarAlumnos);
/* opciElim.addEventListener("click",dialogoEliminarAlumnos); */

/* operAdd.addEventListener("click",AgregarAlumno); */
/* canOperAdd.addEventListener("click",CAgregarAlumno); */

/* operDelete.addEventListener("click",EliminarAlumno);
canOperDelete.addEventListener("click",CEliminarAlumno); */
/* 
msjAgregado.addEventListener("click",cerrarMsjFinalAdd);
msjEliminado.addEventListener("click",cerrarMsjFinalDelete); */


btnShowClose.addEventListener("click",cerraShowStudent);
//funciones
function closeWinAdd(){
    winAdd.classList.toggle('inactivo');
    modifAsesoria.classList.toggle('inactivo');
}
/* function WinDetalle(){
modifAsesoria.classList.toggle('inactivo');
console.log("Detalle")
} */

function WinDetalle_Open_Add(){
    modifAsesoria.classList.toggle('inactivo');
    winAdd.classList.toggle('inactivo');
}

function WinDetalle_Cancel(){
    modifAsesoria.classList.toggle('inactivo');
}

function dialogoAgregarAlumnos(){
    diagOpciAdd.classList.toggle('inactivo');
    winAdd.classList.toggle('inactivo');
}

function dialogoEliminarAlumnos(){
    diagOpciElim.classList.toggle('inactivo');
    modifAsesoria.classList.toggle('inactivo');
}



function AgregarAlumno(){
console.log("Alumno Agregado");
diagOpciAdd.classList.toggle('inactivo');
confdiagOpciAdd.classList.toggle('inactivo');
}


function CAgregarAlumno(){
    diagOpciAdd.classList.toggle('inactivo');
}



function EliminarAlumno(){
    console.log("Alumno Eliminado");
    diagOpciElim.classList.toggle('inactivo');
    confdiagOpciElim.classList.toggle('inactivo');
}

function CEliminarAlumno(){
    diagOpciElim.classList.toggle('inactivo');
}
function cerrarMsjFinalAdd(){
    confdiagOpciAdd.classList.toggle('inactivo');
}
function cerrarMsjFinalDelete(){
    confdiagOpciElim.classList.toggle('inactivo');
}
function cerraShowStudent(){
    modifAsesoria.classList.toggle('inactivo');
}


//Abrir el mensaje ¿Desea inscribirse a la asesoria?
const msjFinalInscripci = document.querySelector('.msj_inscript');
const acepInscri = document.querySelector('.btnACF');
const CmsjFinalIncri = document.querySelector('.btnACCFF');
acepInscri.addEventListener("click",function(){
dialogInscrip.classList.toggle('inactivo');
msjFinalInscripci.classList.toggle('inactivo');

});
const cancelInscri = document.querySelector('.btnCCF');
cancelInscri.addEventListener("click",function(){
    dialogInscrip.classList.toggle('inactivo');
});

CmsjFinalIncri.addEventListener("click",function(){
    msjFinalInscripci.classList.toggle('inactivo');
});