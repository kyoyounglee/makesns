$(document).ready(function(){
	$.ajax({
		url: '/ajax',
		type: 'POST',
		success: function(response){
			$('#post_ajax').append(response);
		},
		error: function(){
			console.log("error");
		},
		complete: function(){
			console.log("complete");
		}

	});
});