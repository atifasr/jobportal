
let createJobButton = document.querySelector('.create_job')



let createSkillDiv = ()=>{
    let skillDivContainer = $('.skillDiv')
    let firstDiv =  $("<div></div>").addClass("col-md-6 mt-2").append(
            $("<input>").addClass("form-control").attr({"type":"text","name":"skill_name","placeholder":"Skill name"})
        )
    
    let secondDiv = $("<div></div>").addClass("col-md-6 mt-2").append(
        $("<select></select>").addClass("form-control").attr({
            "for":"job_skill_name","name":"job_skill_level"
        }).append(
            $("<option></option>").attr({"value":"beginner"}).text('beginner'),
            $("<option></option>").attr({"value":"intermediate"}).text('intermediate'),
            $("<option></option>").attr({"value":"expert"}).text('expert')
        )
    )

    skillDivContainer.append(firstDiv,secondDiv)
    
}



let count_skillbar = 0
$(createJobButton).on('click',function(e){
    console.log('clicked')
    if (count_skillbar < 2)
    {
        createSkillDiv()
    }
    count_skillbar += 1
   
})




