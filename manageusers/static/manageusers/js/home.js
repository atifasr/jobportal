

let Displaynotify = (text) =>{
    $(".message_div").replaceWith(
        $("<div></div>").addClass("alert alert-primary alert-dismissible fade show").attr("role","alert").append(
        $("<strong></strong>").text(text),
            $("<button></button>").attr({"type":"button","aria-label":"Close","data-dismiss":"alert"}).addClass("close").append(
        $("<span></span>").attr({"aria-hidden":"true"}).text("&times;")
            )
        )
    )
}
 



let SubscribeButton = $('.sub_email')

SubscribeButton.on('click',function(){
    user = $('.email_sub').attr("data-user")
    email = $('.email_sub').val()
    cred = {
        email : email,
        user : user
    }
    $.ajax(
        {
            url:'/sub_emailalert/',
            method : 'GET',
            data : cred,
            dataType: "json",
            contentType: "application/json",
            success :function(data){
                console.log(data)
                if (data.status == 'email_dublicated')
                {
                    Displaynotify("email has already been updated !")
                    
                }
                else if (data.status == 'updated')
                {
                    Displaynotify("Email subscribed for news letter!")
                }
            }
            ,
            error:function(e){
                console.log(e)

            }
        }
    )
})