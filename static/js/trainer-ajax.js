
$(document).ready(function() {

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

/*
	$('#complete').click(function() {
  		$(this).hide()
  		$('#next').show()

  		$.get('/trainer_app/log_workout_time/', {'category_id': 'test'},
		function(data) {

			if (data === 'True'){
				alert('hjghg')
			}

		})
	*/

});


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

