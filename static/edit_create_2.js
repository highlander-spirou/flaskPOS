$(document).ready(function(){
    $('.create-wrapper').hide();
    $('.delete-wrapper').hide();
    $('.edit-wrapper').hide();
});



$(document).on('click', '#create', function(){
    $('.create-wrapper').show();
});



$(document).on('click', '#delete', function(){
    $('.delete-wrapper').show();
});



$(document).on('click', '#cancel', function(){
    $('.create-wrapper').hide();
    $('.delete-wrapper').hide();
    $('.edit-wrapper').hide();
});



// hansolTable button có thêm edit

$(document).on('click', '#edit', function(){
    $('.edit-wrapper').show();
});