(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            Swal.fire({
                title: "¿Confirma la eliminación del libro?",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false
            });
        });
    });
})();

