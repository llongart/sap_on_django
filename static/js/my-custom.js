// Cargar configuración de idioma español en datatables e iniciarla
import language from '../json/es-MX.json' with { type: 'json' };

let table = new DataTable('#stockTable', {
    language: language,
    sort: true,
    layout: {
        topStart: {
            buttons: ['pageLength', 'spacer', 'excelHtml5', 'spacer', 'pdf']
        },
        topEnd: { 
            search: {
              placeholder: 'Introducir filtrado' 
            }
        },
        bottomStart: 'info',
        bottomEnd: {
            paging: {
                buttons: 10,
                numbers: true
            }
        }
    }      
});


addMaterialMatchCodeListener()
function addMaterialMatchCodeListener() {
    const buttonMatchCode = document.querySelector('[material-matchcode]');
    buttonMatchCode.addEventListener("click", () => {
        var $matchcode = $("#matchcode");
        var matchcode_url = $("#material-matchcode").val();
        $(".modal-body", $matchcode).load(matchcode_url, function () {
            $matchcode.modal("show");
        });        
    });
}

addArticleGrpMatchCodeListener()
function addArticleGrpMatchCodeListener() {
    const buttonMatchCode = document.querySelector('[article-grp-matchcode]');
    buttonMatchCode.addEventListener("click", () => {
        var $matchcode = $("#matchcode");
        var matchcode_url = $("#article-group-matchcode").val();
        $(".modal-body", $matchcode).load(matchcode_url, function () {
            $matchcode.modal("show");
        });        
    });
}


// Cerrar la modal al presionar guardar
const modal = new bootstrap.Modal('#matchcode');

document.querySelector('#guardar').addEventListener('click', () => {
    modal.hide();
});

// var myModal = document.getElementById('matchcode')
// var myInput = document.getElementById('closeButton')

// myModal.addEventListener('shown.bs.modal', function () {
//   myInput.focus()
// })