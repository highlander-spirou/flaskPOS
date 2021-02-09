$(document).ready(function(){
    $('.edit-wrapper').hide();
    $('.delete-wrapper').hide();
});

$(document).on('click','.btn_edit', function(){

    $('.edit-wrapper').show();
    var currentRow=$(this).closest("tr");

    var col1=currentRow.find("td:eq(0)").text();
    var col2=currentRow.find("td:eq(1)").text();
    var col3=currentRow.find("td:eq(2)").text();
    var col4=currentRow.find("td:eq(3)").text();
    var col5=currentRow.find("td:eq(4)").text();
    var col6=currentRow.find("td:eq(5)").text();
    var col7=currentRow.find("td:eq(6)").text();
    var col8=currentRow.find("td:eq(7)").text();
    var col9=currentRow.find("td:eq(8)").text();
    var col10=currentRow.find("td:eq(9)").text();
    var col11=currentRow.find("td:eq(10)").text();
    var col12=currentRow.find("td:eq(11)").text();
    var col13=currentRow.find("td:eq(12)").text();
    var col14=currentRow.find("td:eq(13)").text();
    var col15=currentRow.find("td:eq(14)").text();

    console.log(`${col2}, ${col3}, ${col4}, ${col5}, ${col6}, ${col7}`)
    
    $('#idEdit').val(col1);
    $('#bill_numberEdit').val(col2);
    $('#shipper_nameEdit').val(col3);
    $('#consignee_nameEdit').val(col4);
    $('#client_nameEdit').val(col5);
    $('#consignee_addressEdit').val(col6);
    $('#consignee_telephoneEdit').val(col7);
    $('#cargo_pcsEdit').val(col8);
    $('#cargo_weightEdit').val(col9);
    $('#pp_ccEdit').val(col10);
    $('#hs_codeEdit').val(col11);
    $('#cargo_itemEdit').val(col12);
    $('#invoice_valueEdit').val(col13);
    $('#bag_numberEdit').val(col14);
    $('#zipcodeEdit').val(col15);
});

$(document).on('click', '.btn_delete', function(){
    $('.delete-wrapper').show();
});

$(document).on('click', '.btn_cancel', function(){
    $('.edit-wrapper').hide();
    $('.delete-wrapper').hide();
});