
$(document).ready(function() {

$('.icon').click(function() {
    var unit_id_var;
    unit_id_var = $(this).attr('data-unitid');
    $.get('/circuit_complete',
        {'unit_id': unit_id_var}, function(data) {
            alert(data)
    })
});


var allimages= document.getElementsByTagName('img');
    for (var i=0; i<allimages.length; i++) {
        if (allimages[i].getAttribute('data-src')) {
            allimages[i].setAttribute('src', allimages[i].getAttribute('data-src'));
        }
    }




/*
function pageLoad() {
    var nodeList, index;
    nodeList = document.body.getElementsByTagName('img');
    index = 0;
    backgroundLoader();

    function backgroundLoader() {
        var img, src;
        if (index >= nodeList.length) {
            return;
        }
        img = nodeList[index];
        src = img.getAttribute("data-src");
        if (src) {
            // It's one of our special ones
            img.src = src;
            img.removeAttribute("data-src");
        }
        ++index;
        window.setTimeout(backgroundLoader, 200);
    }
}    

pageLoad()
*/

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

