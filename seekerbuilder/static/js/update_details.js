

// Jquery check
if (typeof(jQuery) == 'undefined'){
    console.log('not loaded')
}
else{
    console.log('working')
}


let add = $(".add_ins")

$(add).on('click', function (e) {
    console.log('clicked')
    
});

add.on('click',function(e){
    
    console.log('working')
})