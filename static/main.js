

var room = '1';



$(function(){ 
    

    console.log('main.js is running.')


    // prime the interface with starting room
    update_room_info(room)

    // event handlers begin
    $(document).on('click', '#go', function(event){
        var my_dir = $('#command').val()
        navigate(room, my_dir);
    });

    $(document).on('click', '.direction-button', function(event){
        var my_dir = event.target.getAttribute("data-dir");
        if (my_dir == '' || my_dir == undefined){
            // do nothing
        }else{
            navigate(room, my_dir);
        }
        
     });

    $(document).on('mouseover', '.direction-button', function(event){
        console.log('hovering')
        var my_dir = event.target.getAttribute("data-dir");
        $('#command').val('');
        $('#command').val(my_dir);
    })
    
    
    
    
     // functions begin
    function update_room_info(room_id){
        my_url = "http://127.0.0.1:5000/room/"+room
        $.ajax({
            url: my_url,
            type: 'GET',
            success: function(res) {      
                my_json = JSON.parse(res);

                var name = my_json.name;
                var short_desc = my_json.short_desc;
                var long_desc = my_json.long_desc;
                var travel = my_json.travel;
                var image = my_json.image;

                $('#room-image').attr('src', 'img/'+image);
                $('#room_info').html(
                    '<p>Room Name: ' + name + '</p>' +
                    '<p>Short Description: ' + short_desc + '</p>' +
                    '<p>Long Description: ' + long_desc + '</p>' +
                    '<p>Travel Description: ' + travel.join('-') + '</p>'
                );

            }
        });
    }
 

    function navigate(my_room, my_dir){
         my_url = "http://127.0.0.1:5000/adventure/"+my_room+","+my_dir
         $.ajax({
             url: my_url,
             type: 'GET',
             success: function(res) {      
                 my_json = JSON.parse(res);

                 // update room global
                 room = my_json.current_room;
                 update_room_info(my_room);
                 $('#command').val('');
 
             }
         });
    }



});
