
var num = 0;
var running = false;

$(document).ready(function(){

	get_posts_in_newsfeed(num);
	console.log('here');



$(window).scroll(function(){
	if (running) return false;


	if ($(window).scrollTop() + $(window).height() == $(document).height())
	{
		num+=5;
		get_posts_in_newsfeed(num);

	}

});

});

function get_posts_in_newsfeed(start_index)
{
	running = true;
	$.ajax({
		url: '/get_newsfeed',
		type: 'POST',
		data: {"num": start_index},
		success: function(response){
			if (response.trim == '')
			{
				$(window).unbind('scroll');
			}
			else
			{
				$('#newsfeed_list').append(response);
				console.log('return');
			}
			

		},
		error: function(){
			console.log('error');
		},
		complete: function(){
			console.log('complete');
			running = false;
		}
	})
}