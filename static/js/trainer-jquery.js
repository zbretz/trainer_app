
$(document).ready(function() {

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

var homework = document.getElementById('homework');
var homework_elems = document.getElementsByClassName("expand-compress")
var circuit = document.getElementsByClassName("circuit");
var x;

homework.addEventListener("click", function(){

	for (x = 0; x < circuit.length; x++) {
		if (circuit[x].style.display === "block") {
      	circuit[x].style.display = "none";
    	} else {
      	circuit[x].style.display = "block";
    	}
	}

	for (x = 0; x < homework_elems.length; x++) {
		homework_elems[x].classList.toggle("hide")
	}

});

var icons = document.getElementsByClassName("icon");
var y;
	
for (y = 0; y < icons.length; y++) {
  icons[y].addEventListener("click", function() {
    this.classList.toggle("w3-grayscale-max")
  });
}

/*
var car = document.getElementsByClassName("cardio");
var c;

var cardio_selection = document.getElementById('cardio-selection')
var extra_cardio = document.getElementById('extra-cardio')

for (c = 0; c < car.length; c++) {
  car[c].addEventListener("click", function() {
    extra_cardio.classList.toggle("hide")
    cardio_selection.classList.toggle("hide")
    document.getElementById('cardio-type-heading').innerHTML = this.innerHTML
  });
}
*/



/* ---------------------WARMUP START---------------------- */
var warm = document.getElementsByClassName("warmup");
var w;

//var cardio_selection = document.getElementById('cardio-selection')
var extra_warmup = document.getElementById('extra-warmup')

for (w = 0; w < warm.length; w++) {
  warm[w].addEventListener("click", function() {
    extra_warmup.classList.toggle("hide")
//    cardio_selection.classList.toggle("hide")
	var selection = this.getAttribute("data-warmuptype")
	document.getElementById(selection).classList.toggle("hide")
  });
}

var warm_cat = document.getElementsByClassName("warmup-category");
var rs
var reselect_warmup = document.getElementsByClassName('reselect-warmup-btn');
for (rs = 0; rs < reselect_warmup.length; rs++) {
  reselect_warmup[rs].addEventListener("click", function() {
	extra_warmup.classList.toggle("hide");
	this.parentElement.classList.toggle("hide")
	});
}
/* ---------------------WARMUP END--------------------- */

/* ---------------------CARDIO START--------------------- */
var car = document.getElementsByClassName("cardio");
var c;
var extra_cardio = document.getElementById('extra-cardio')

for (c = 0; c < car.length; c++) {
  car[c].addEventListener("click", function() {
    extra_cardio.classList.toggle("hide")
//    cardio_selection.classList.toggle("hide")
	var selection = this.getAttribute("data-cardiotype")
	document.getElementById(selection).classList.toggle("hide")
  });
}

var car_cat = document.getElementsByClassName("cardio-category");
var rs
var reselect_cardio = document.getElementsByClassName('reselect-cardio-btn');
for (rs = 0; rs < reselect_cardio.length; rs++) {
  reselect_cardio[rs].addEventListener("click", function() {
	extra_cardio.classList.toggle("hide");
	this.parentElement.classList.toggle("hide")
	});
}
/* ---------------------CARDIO END ---------------------*/

})
