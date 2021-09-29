

// applying for indeed jobs

let Applybutton = document.querySelector('.direct_link')

Applybutton.addEventListener('click',(e)=>{
    e.preventDefault()
    console.log('working')
    let jobpost_id = e.target.getAttribute('data-job')
    console.log(jobpost_id)
    $.ajax({
        url: '/apply_job_in/',
                method : 'POST',
                dataType: 'json',
                data:JSON.stringify(
                    {
                        job_id:jobpost_id,
                    }
                ),
                contentType: 'application/json;charset=utf-8',
                success : function(data){
                    console.log(data)
                },

                error: function(data){
                    console.log(data)
                }


    })

})