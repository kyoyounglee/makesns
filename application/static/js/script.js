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

	var num = 0;

	$(window).scroll(function(){

		if ($(window).scrollTop() + $(window).height() == $(document).height())
		{
			num+=5
			$.ajax({
				url: '/ajax_again',
				type: 'POST',
				data: {"num":num},
				success: function(response){
					if (response.trim() =='')
					{
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

});