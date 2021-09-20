
let createJobButton = document.getElementsByClassName('create_job')[0]



let createSkillDiv = ()=>{
    let skillDivContainer = $('.skillDiv')
    let firstDiv =  $("<div></div>").addClass("col-md-6 mt-2").append(
            $("<input>").addClass("form-control").attr({"type":"text","name":"skill_name","placeholder":"Skill name"})
        )
    
    let secondDiv = $("<div></div>").addClass("col-md-6 mt-2").append(
        $("<select></select>").addClass("form-control").attr({
            "for":"job_skill_name"
        }).append(
            $("<option></option>").attr({"value":"beginner"}).text('beginner'),
            $("<option></option>").attr({"value":"intermediate"}).text('intermediate'),
            $("<option></option>").attr({"value":"expert"}).text('expert')
        )
    )

    skillDivContainer.append(firstDiv,secondDiv)
    
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