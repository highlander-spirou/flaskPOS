


$(document).ready(function(){
    $.getJSON('/tabledata', function(data) {
        var tableData = '';
        $.each(data, function(key, value){
            tableData += '<tr row_id="'+value.id+'">';
            tableData += '<td><div contenteditable="true">'+value.id+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.bill_number+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.shipper_name+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.consignee_name+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.client_name+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.consignee_address+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.consignee_telephone+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.cargo_pcs+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.cargo_weight+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.pp_cc+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.hs_code+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.cargo_item+'</div></td>';    
            tableData += '<td><div contenteditable="true">'+value.invoice_value+'</div></td>'; 
            tableData += '<td><div contenteditable="true">'+value.bag_number+'</div></td>'; 
            tableData += '<td><div contenteditable="true">'+value.zipcode+'</div></td>'; 
            tableData += '<td><button class="btn btn-outline-secondary"><span class="btn_edit">Edit</span></button></td>';
            tableData += '<td><button class="btn btn-outline-danger"><span class="btn_delete">Delete</span></button></td>';
            tableData += '<td><button class="btn btn-warning"><span class="btn_cancel">Cancel</span></button></td>';
            tableData += '</tr>';
        });
        $('#table-data').append(tableData);
    })
    
});

