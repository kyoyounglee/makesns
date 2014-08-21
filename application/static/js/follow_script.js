var abort_command ;

$(document).ready(function(){
	$('input[name=search_name]').keyup(function(){

		$('#find_user').empty();

		if (abort_command)
		{
			abort_command.abort();
		}

		var key = $('input[name=search_name]').val();

		if (key=='')
		{
			$('#find_user').empty();
		}

		else
		{
			abort_command = $.ajax({
				url: '/follow',
				type: 'POST',
				data: {"key": key},
				success: function(response){
					$('#find_user').append(response);
					console.log('success');
				},
				error: function(){
					console.log('error');
				},
				complete: function(){
					console.log('complete');
				}
			});
		}
	});
});