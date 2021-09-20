

let jobSave = document.querySelectorAll('.save_job')

jobSave.forEach((element)=>{
    element.addEventListener('click',(e)=>{
        let id = e.target.getAttribute("data-job")
        let us_job = e.target.getAttribute("data-user")
        if (us_job != 'AnonymousUser')
        {
            $.ajax({
                url: '/save_job/',
                method : 'GET',
                data: {
                    id:id,
                    us_job:us_job
                },
                dataType: "json",
                contentType: "application/json",
                success :function(data){
                    console.log(data)
                    if (data.saved)
                    {
                        $(".message_div").replaceWith(
                            $("<div></div>").addClass("alert alert-primary alert-dismissible fade show").attr("role","alert").append(
                            $("<strong></strong>").text("job Already saved"),
                                $("<button></button>").attr({"type":"button","aria-label":"Close","data-dismiss":"alert"}).addClass("close").append(
                            $("<span></span>").attr({"aria-hidden":"true"}).text("&times;")
                                )
                            )
                        )
                        console.log('job is already saved')
                    }
                    else{
                        console.log('job saved')
                        $(".message_div").replaceWith(
                            $("<div></div>").addClass("alert alert-primary alert-dismissible fade show").attr("role","alert").append(
                            $("<strong></strong>").text("job saved!"),
                                $("<button></button>").attr({"type":"button","aria-label":"Close","data-dismiss":"alert"}).addClass("close").append(
                            $("<span></span>").attr({"aria-hidden":"true"}).text("&times;")
                                )
                            )
                        )
                    }
                },
                error: function (xhr) {
                    console.log(xhr.error);
                  },
                
            })
        }
        else{
            console.log('kindly sign in')
            
            let div = $("<div></div>").addClass("alert alert-warning alert-dismissible fade show").attr("role","alert").append(
                    $("<strong></strong>").text("Kindly Sign in before saving "),
                     $("<button></button>").attr({"type":"button","aria-label":"Close","data-dismiss":"alert"}).addClass("close").append(
                    $("<span></span>").attr({"aria-hidden":"true"}).text("&times;")
                     )
                    )
            $(".message_div").append(div)
        }
    })

})


