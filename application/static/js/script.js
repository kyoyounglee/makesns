
//var last = false;
var num = 0;
var running = false;

$(document).ready(function(){

	get_posts(num);
	// $.ajax({
	// 	url: '/ajax', // /get_posts
	// 	type: 'POST',
	// 	success: function(response){
	// 		$('#post_ajax').append(response);
	// 	},
	// 	error: function(){
	// 		console.log("error");
	// 	},
	// 	complete: function(){
	// 		console.log("complete");
	// 	}
	// });


$(window).scroll(function(){
	if (running) return false;


	if ($(window).scrollTop() + $(window).height() == $(document).height())
	{
		num+=5;
		get_posts(num);

	}

});



});


function get_posts(start_index)
{
	running = true;
	$.ajax({
		url: '/ajax_again',
		type: 'POST',
		data: {"num":start_index},
		success: function(response){
			if (response.trim() =='')
			{
				//last=true;
				$(window).unbind('scroll');
			} else 
			{
				$('#post_ajax').append(response);
				console.log('return');
			}
		},
		error: function(){
			console.log('error');
		},
		comlete: function(){
			console.log('complate');
			running = false;
		}
	})
}