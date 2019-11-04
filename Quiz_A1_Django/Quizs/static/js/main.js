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
	$('.0').css('display','block')
	$('.btnPrev').click(function(){
		var checkQuesionNum = $('#inputIndex').val()
		if(checkQuesionNum == 0){
			$('.9').css('display','block')
			$('.0').css('display','none')
			$('#inputIndex').val(9)

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

	$('.btnNext').click(function(){
		var checkQuesionNum = $('#inputIndex').val()
		if(checkQuesionNum == 9){
			$('.9').css('display','none')
			$('.0').css('display','block')
			// var tempClass3 = '#inputValueQuestion'+checkQuesionNum
			// $(tempClass3).val($('#valueAnser').val())
			$('#inputIndex').val(0)

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
			}
		},1000)

});
