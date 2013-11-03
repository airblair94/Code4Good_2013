$(document).ready(function() {
///////////////////////

$(document).on("click", ".formLink", function(e) {
	e.preventDefault(); //Don't continue with the default link.
	
	var address = $(this).attr("href");
	$.get(address, function(response) {
		$("#main-content").html(response);
	});	
});

$(document).on("submit", ".appForm", function(e) {
	e.preventDefault();
	var form = $(this);
	$.post($(form).attr("action"), $(form).serialize(), function(response) {
		$(form).parent().html(response);
	});	
});

$(document).on("submit", ".loginForm", function(e) {
	e.preventDefault();
	var form = $(this);
	$.post($(form).attr("action"), $(form).serialize(), function(response) {
		$("#left-bar").html(response);
		if ($(".successIndicator").length>0){
			setTimeout("location.reload(true);", 20);
		}
	});	
});

////////////////////////
});
