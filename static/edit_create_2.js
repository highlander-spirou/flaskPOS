$(document).ready(function(){
    $('.delete-wrapper').hide();
    $('.edit-wrapper').hide();
});




$(document).on('click', '#delete', function(){
    $('.delete-wrapper').show();
});



$(document).on('click', '#cancel', function(){
    $('.delete-wrapper').hide();
    $('.edit-wrapper').hide();
});



// hansolTable button có thêm edit

$(document).on('click', '#edit', function(){
    $('.edit-wrapper').show();
});