$(document).ready(function(){
	$('#goModalRe').click(function(){
		// $('#formRegister').trigger("reset");
		// $('#formLogin').trigger("reset");
		// $('#formRegister')[0].reset()
		// $('#formLogin')[0].reset()
		$('#modalRegister').modal('hide')
		$('#modalLogin').modal('show')
	})

	$('#goModalLog').click(function(){
		// console.log($('#formRegister')[0])
		// $('#formRegister')[0].reset()
		// $('#formLogin')[0].reset()
		$('#modalRegister').modal('show')
		$('#modalLogin').modal('hide')
	})

	$('#dateOfBirth').datepicker({
	});
})