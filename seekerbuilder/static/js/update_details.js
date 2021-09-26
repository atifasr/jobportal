

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
            $("<input/>").attr({"type":"text","placeholder":"skill name","name":"skill_name"}).addClass("form-control skill_name")
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






// deleting skills 

let delete_class_list = $('.delete_skill')
delete_class_list.click(function(e){
    let value = this.getAttribute("data-attr")
    console.log(value)
    let contain_icon = this
    let contain_label = contain_icon.parentElement.previousSibling
    console.log(contain_label)
    $.ajax({
        url:'/delete_skill/',
        method : 'POST',
        data: JSON.stringify(
            {
                skill_id : value
            }
        ),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success :function(data){
            console.log(data)
            contain_label.remove()
            contain_icon.remove()   
        }
        ,
        error:function(e){
            console.log(e)

        }
    })
})

// let len = delete_class_list.length
// for ( let i = 0 ; i< len ; i++)
// {
//     delete_class_list[i].bind('click',function(){
//         e.preventDefault()
//         console.log('working')
//     })

// }










// saving and updating skills
$('div.save_contain').on('click',function(e){
    e.preventDefault()
    let select_list = $('select.custom-select')
    let skill_names = $('input.skill_name')
    
    if (e.target.nodeName == 'BUTTON')
    {
        console.log('data updated')
        let SeekerSkillData = []
        select_list.each((ind,element)=>{
            console.log(skill_names[ind].value,element.value)
            obj = {
                skill_name : skill_names[ind].value,
                skill_level : element.value
            }
            SeekerSkillData.push(obj)

            })

            $.ajax({
                url:'/add_skill/',
                method : 'POST',
                data : JSON.stringify(
                    SeekerSkillData
                ) ,
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                success :function(data){
                    console.log(data)
                }
                ,
                error:function(e){
                    console.log(e)

                }
            })

            console.log(SeekerSkillData)
            location.reload(); 
    }

})



