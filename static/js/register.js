function validar() {
    var nombre = document.getElementById("Nombre").value;
    var email = document.getElementById("Email").value;
    var edad = document.getElementById("Edad").value;
    

    if (nombre.length <= 0 || nombre.length > 15) {
        document.getElementById('lNombre').innerHTML = "ingrese un nombre";
        document.getElementById('lNombre').style.color = 'red';
        return
    } else {
        document.getElementById('lNombre').innerHTML = "ok!";
        document.getElementById('lNombre').style.color = 'green';
    }
    if (email.length <= 0 || email.length > 30) {
        document.getElementById('lEmail').innerHTML = "error en el campo de correo";
        document.getElementById('lEmail').style.color = 'red';
        return
    } else {
        document.getElementById('lEmail').innerHTML = "ok!";
        document.getElementById('lEmail').style.color = 'green';
    }
    if (!parseInt(edad)) {
        document.getElementById('lEdad').innerHTML = "El campo de edad debe ser un numero";
        document.getElementById('lEdad').style.color = 'red';
        return
    }  
    if (edad <= 10 || edad > 99) {
        document.getElementById('lEdad').innerHTML = "edad no valida, debes tener 10 años";
        document.getElementById('lEdad').style.color = 'red';
        return
    } else {
        document.getElementById('lEdad').innerHTML = "ok!";
        document.getElementById('lEdad').style.color = 'green';
    }
    
    document.getElementById('principal').innerHTML = "FELICIDADES " + nombre + " TE HAS REGISTRADO CON EXITO!!";
};