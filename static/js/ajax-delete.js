
$(document).ready(function() {


	$('#complete').click(function() {
  		$(this).hide()
  		$('#next').show()

  		$.get('/trainer_app/log_workout_time/', {'category_id': 'test'},
		function(data) {
			alert(data);

			if (data === 'True'){
				alert(data)
				$("#next_button").removeClass('disabled')
				alert('gabagoo')
			}

		})

	});

	$('#next').click(function() {

  		$.get('/trainer_app/time_check/', {'category_id': 'test'},
		function(data) {
			if (data === 'True'){
				alert(data + 'yes')
				$("#next_button").removeClass('disabled')
				$("#next_button").click()


			} else {
				alert(data)
				alert('7Please wait until your next Gym Day.')
			}

			if (data === 'True'){
				

 				}else{}
			
		})

	})


/*	
	$('#like_btn').click(function() {
	var category_id_var;
	category_id_var = $(this).attr('data-categoryid');

	$.get('/rango/like_category/', {'category_id': category_id_var},
		function(data) {
			$('#like_count').html(data);
    		$('#like_btn').hide();
		})
	});

*/	
});

