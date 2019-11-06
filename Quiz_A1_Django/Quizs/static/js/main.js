$(document).ready(function() {
	// executes when HTML-Document is loaded and DOM is ready
	// function btnClick(a){
	// 	alert("HHH")
	// }
	var now = new Date().getTime();
	// var now = 0;
	var endExamp = now + 1000*15*60
	// function coutDown(){
	// document.getElementsByClassName('mainQuestion')[0].style.display = 'block'
	$('.1').css('display','block')
	$('.btnPrev').click(function(){
		var checkQuesionNum = $('#inputIndex').val()
		if(checkQuesionNum == 1){
			$('.10').css('display','block')
			$('.1').css('display','none')
			$('#inputIndex').val(10)

		}
		else{
			var tempClass = '.'+checkQuesionNum
			$(tempClass).css('display','none')
			checkQuesionNum = Number(checkQuesionNum)-1
			var tempClass2 = '.'+checkQuesionNum
			$(tempClass2).css('display','block')
			$('#inputIndex').val(checkQuesionNum)		
		}

	})	

	function abc(a){
		alert(a.value)
	}

	$('#btnSubmit').click(function(){
		alert($('#valueAnser').val())

	})



	$('.btnNext').click(function(){
		var checkQuesionNum = $('#inputIndex').val()
		if(checkQuesionNum == 10){
			$('.10').css('display','none')
			$('.1').css('display','block')
			// $('#btnNum0').css('background-color','green')
			// var tempClass3 = '#inputValueQuestion'+checkQuesionNum
			// $(tempClass3).val($('#valueAnser').val())
			$('#inputIndex').val(1)

		}
		else{
			var tempClass = '.'+checkQuesionNum
			$(tempClass).css('display','none')
			checkQuesionNum = Number(checkQuesionNum)+1
			var tempClass2 = '.'+checkQuesionNum
			$(tempClass2).css('display','block')
			$('#inputIndex').val(checkQuesionNum)
		}
	})


	$('#btnNum2').click(function(){
		alert(this.value)
		console.log($('#btnNum2'))
	})

	var x = setInterval(function coutDown(){
			var now = new Date().getTime()
			var dis = endExamp - now

			var min = Math.floor(dis/(1000*60))
			var second = Math.floor((dis%(1000*60)/1000))
			$(".spanCountDown").text(min + " Phút : " + second + "giây")

			if (dis < 0){
				clearInterval(x)
				$(".spanCountDown").text("Hết giờ")
				alert("Đã hết giờ làm bài !!")		

			}
		},1000)

});
