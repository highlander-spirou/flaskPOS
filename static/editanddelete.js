$(document).ready(function(){
    $('.edit-wrapper').hide();
    $('.delete-wrapper').hide();
});

$(document).on('click','.btn_edit', function(){

    $('.edit-wrapper').show();
    var currentRow=$(this).closest("tr");

    var col2=currentRow.find("td:eq(1)").text();
    var col3=currentRow.find("td:eq(2)").text();
    var col4=currentRow.find("td:eq(3)").text();
    var col5=currentRow.find("td:eq(4)").text();
    var col6=currentRow.find("td:eq(5)").text();
    var col7=currentRow.find("td:eq(6)").text();

    console.log(`${col2}, ${col3}, ${col4}, ${col5}, ${col6}, ${col7}`)
    
    $('#nameInput').val(col2);
    $('#ageInput').val(col3);
    $('#roleInput').val(col4);
    $('#companyInput').val(col5);
    $('#cityInput').val(col6);
    $('#zipInput').val(col7);
});

$(document).on('click', '.btn_delete', function(){
    $('.delete-wrapper').show();
});

$(document).on('click', '.btn_cancel', function(){
    $('.edit-wrapper').hide();
    $('.delete-wrapper').hide();
});