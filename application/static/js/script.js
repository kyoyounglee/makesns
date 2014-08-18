
var last = false;
var num = 0;

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


	$(window).scroll(function(){
		if (last) return false;

		if ($(window).scrollTop() + $(window).height() == $(document).height())
		{
			num+=5;
			get_posts();

		}

	});

	function get_posts()
	{
		$.ajax({
			url: '/ajax_again',
			type: 'POST',
			data: {"num":num},
			success: function(response){
				if (response.trim() =='')
				{
					last=true;
					return false;
				}

				$('#post_ajax').append(response);
				console.log('return');
			},
			error: function(){
				console.log('error');
			},
			comlete: function(){
				console.log('complate');
			}
		})
	}

});