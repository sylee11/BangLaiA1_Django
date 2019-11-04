$(document).ready(function(){
	function abc(a){
		alert(a.value)
	}

	$('#goModalRe').click(function(){
		$('#modalRegister').modal('hide')
		$('#modalLogin').modal('show')
	})

	$('#goModalLog').click(function(){
		$('#modalRegister').modal('show')
		$('#modalLogin').modal('hide')
	})

	//Clear input
	$('.inputEmail').click(function(){
		$('.messageError').hide()

	})


	$('#dateOfBirth').datepicker({
	});

	//show erro
	valError = $('#inputError').val()
	if(valError == 'UserLoginFail'){
		$('#modalRegister').modal('hide')
		$('#modalLogin').modal('show')
	}
	else if(valError == 'User has exists'){
		$('#modalRegister').modal('show')
		$('#modalLogin').modal('hide')
	}	
	else if(valError == 'requireLogin'){
		$('#modalRegister').modal('hide')
		$('#modalLogin').modal('show')
	}



})