$(document).ready(function(){
    $('.create-wrapper').hide();
    $('.delete-wrapper').hide();
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
});