


$(document).ready(function(){
    $.getJSON('/tabledata', function(data) {
        var tableData = '';
        $.each(data, function(key, value){
            tableData += '<tr row_id="'+value.id+'">';
            tableData += '<td><div contenteditable="true">'+value.id+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.name+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.age+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.role+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.company+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.city+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.zipcode+'</div></td>';
            tableData += '<td><button class="btn btn-outline-secondary"><span class="btn_edit">Edit</span></button></td>';
            tableData += '<td><button class="btn btn-outline-danger"><span class="btn_delete">Delete</span></button></td>';
            tableData += '<td><button class="btn btn-warning"><span class="btn_cancel">Cancel</span></button></td>';
            tableData += '</tr>';
        });
        $('#table-data').append(tableData);
    })
    
});

