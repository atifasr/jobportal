
let createJobButton = document.getElementsByClassName('create_job')[0]



let createSkillDiv = ()=>{
    let skillDivContainer = $('.skillDiv')
    
    
}



let count = 0
$(createJobButton).on('click',function(e){

    if (count < 2)
    {
        createSkillDiv()
        console.log('skill bar added')
    }
    count += 1
    console.log('clicked')
})