

// Jquery check
if (typeof(jQuery) == 'undefined'){
    console.log('not loaded')
}
else{
    console.log('working')
}


let add_skill = $(".add_skill_grp")
let add_details = $(".add_ins")

// adding skills container
let addSkillsContainer = () =>{
  
    let div_contain =$("<div></div")
    div_contain.addClass("col-md-5")
    div_contain.append(
        $("<div></div").addClass("form-group input-group").append(
            $("<input/>").attr({"type":"text","placeholder":"skill name","name":"skill_name"}).addClass("form-control")
        )
    )
    let div_Select = $("<div></div>")
    div_Select.addClass("col-md-5").append(
        $("<select></select>").addClass("custom-select").attr("name","skill_level").append(
            $("<option></option>").attr("value","beginner").text("beginner"),
            $("<option></option>").attr("value","intermediate").text("intermediate"),
            $("<option></option>").attr("value","advance").text("advance")
        )
    )

    let form_contain = $("<div></div>").addClass("form-row")

    let main_container = $(".main-contain").eq(0)
    form_contain.append(div_contain,div_Select)
    main_container.after(form_contain)
}



let addDetails= () =>{
    let div_contain =$("<div></div")

}


// event for calling skills add function
let countSkill_cont = 0
$(add_skill).on('click', function (e) {
    e.preventDefault()
    if (countSkill_cont < 3)
    {
        addSkillsContainer()
        countSkill_cont += 1
    }
});

$(add_details).on('click',function(){
    console.log('working')
})



