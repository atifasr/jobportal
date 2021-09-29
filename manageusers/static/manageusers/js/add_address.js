
let count_address = 0
$('.add_addresstab').click(function(e){
    if (count_address < 1)
    {
        $('.address-container').append(
            $('<div></div>').addClass('form-group col-md-4').append(
                $('<label></label>').attr("for","inputAddress").text("Address"),
                $('<input></input>').attr({"name":"address_street","type":"text"}).addClass("form-control")
                
                ),
            $('<div></div>').addClass('form-group col-md-8').append(
                $('<div></div>').addClass('form-row').append(
                    $('<div></div>').addClass('form-group col-md-4').append(
                        $('<label></label>').attr('for','inputCity').text('City'),
                        $('<input></input>').attr({"name":"city","type":"text"}).addClass('form-control')
                    ),
                    $('<div></div>').addClass('form-group col-md-4').append(
                        $('<label></label>').attr("for","inputState").text("State"),
                        $("<select></select>").attr("name","state").addClass("form-control").append(
                            $('<option></option>').attr("value","udaipur").text("udaipur"),
                            $('<option></option>').attr("value","West bengal").text("West bengal"),
                            $('<option></option>').attr("value","jammu and kashmir").text("jammu and kashmir"),
                            $('<option></option>').attr("value","haryana").text("haryana")
                        )

                    ),
                    $('<div></div>').addClass('form-group col-md-4').append(
                        $('<label></label>').text("Zip"),
                        $('<input></input>').attr({"type":"text","name":"zip_code"}).addClass("form-control")
                    )
                )
            )

        )

    }
    count_address += 1
    

})