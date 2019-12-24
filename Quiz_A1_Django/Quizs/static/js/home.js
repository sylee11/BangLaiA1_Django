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


	$('#btnSendComment').click(function(){
		var contentCmt = $('#textareaComment').val()
		var idUser = $('#inputHiddenUser').val()
		alert(contentCmt)
		$.ajax({
			url : 'comment',
			datatype: JSON,
			type : 'POST',
			data: {
				'valueContentCmt' : contentCmt,
				'valueIdUser' : idUser,
			},
			success: function(data){
				$('#textareaComment').val('')
				$('#contentComment').html('')
				for(var i =0; i<data.length; i++){
					$('#contentComment').append('<div class="row" > <div class="col-2"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmYxBq3_IN4hEMn0u6Ql_BAPdCUUGYT_uC9Q0kUYQ4o7BYGLMx&s" alt="avatar"  style="width: 50px; height: 50px; border-radius:50%; "></div><div class="col-10"><span>'+data[i].idUser__name+'</span><br><span>'+data[i].comment+'</span><br><span style="font-size: 12px; font-weight:inherit;color:#138496  ">'+data[i].time+'</span><a style="font-size: 12px;margin-left: 20px; " href="#">like</a> <i style="color: blue" class="fas fa-thumbs-up"></i></div></div>')
				}
			},
			error: function(data){

			},
		})
	})
})