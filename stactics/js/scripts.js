$(document).ready(function(){

    // Modal

    $(document).on("click", ".modal", function (e) {
        if (($(e.target).hasClass("modal-main") ||
            $(e.target).hasClass("close-modal")) && $("#loading").css("display") == "none") {
            closeModal();
        }
    });

    // -> Modal

    //Se abre el panel para poder seleccionar la foto
    $(document).on("click", ".up-img", function () {
        $("#archivo").click();
    });

    function mostrarImagen(event){
        var imagenSource = event.target.result;
        let previewImage = document.getElementById('preview');
        previewImage.src = imagenSource;
    }

    function procesarArchivo(event){
        var imagen = event.target.files[0];
        var lector = new FileReader();
        lector.addEventListener('load', mostrarImagen, false)
        lector.readAsDataURL(imagen);
    }

    document.getElementById('archivo')
        .addEventListener('change', procesarArchivo, false)



})();