const alertList = document.querySelectorAll('.alert');

alertList.forEach(function (alert) {
    new bootstrap.Alert(alert)
})

$(document).ready(() => {
    $('.datetimeinput').datetimepicker({
        format: 'd/m/Y H:i',
    })
    ;
    $.datetimepicker.setLocale('pt-BR');


    setTimeout(() => {
        $(".alert").alert('close');
    }, 3000);
});