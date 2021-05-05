
function mostrarRolEmpresa() {
    element = document.getElementById("rolempresa"),
    check = document.getElementById("soyempresa")
    if (check.checked) {
        element.style.display='block';
    }
    else {
        element.style.display='none';
    }
}
