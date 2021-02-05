


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
            tableData += '<td><button class="btn_edit"><a class="btn btn-link">Edit</a></button></td>';
            tableData += '<td><button class="btn_delete"><a class="btn btn-link">Delete</a></button></td>';
            tableData += '<td><button class="btn_cancel"><a class="btn btn-link">Cancel</a></button></td>';
            tableData += '</tr>';
        });
        $('#table-data').append(tableData);
    })
    
});

