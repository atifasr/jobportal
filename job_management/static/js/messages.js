

let MessagesContain = $('.open_message')

MessagesContain.on('click',function(e){
    console.log('working')
    let sender = e.target.getAttribute("data-sender")
    let receiver = e.target.getAttribute("data-recp")
    $('.recp_name').text(`send to ${receiver}`)
    let send_button = $('.sub_email')
    
    send_button.click(function(e){
        let message = $('textarea.email_sub').val()
       
        $.ajax(
            {
                url: '/send_message/',
                method : 'POST',
                dataType: 'json',
                data:JSON.stringify(
                    {
                        sender:sender,
                        receiver:receiver,
                        message:message
                    }
                ),
                contentType: 'application/json;charset=utf-8',
                success : function(data){
                    console.log(data)
                },
                error:function(error){
                    console.log(error)
                }
            }
        )
        
    })
   
})