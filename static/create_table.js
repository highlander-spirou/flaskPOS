
$(document).ready(function(){
    $.getJSON('/tabledata', function(data) {
        var tableData = '';
        $.each(data, function(key, value){
            tableData += '<tr>';
            tableData += '<td><div contenteditable="true">'+value.name+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.age+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.role+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.company+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.city+'</div></td>';
            tableData += '<td><div contenteditable="true">'+value.zipcode+'</div></td>';
            tableData += '</tr>';
        });
        $('#table-data').append(tableData);
    })
    let div = document.querySelectorAll('div');
    div.focus();
});
