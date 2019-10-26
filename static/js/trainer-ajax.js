
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

