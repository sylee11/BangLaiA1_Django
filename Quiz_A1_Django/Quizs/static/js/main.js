$(document).ready(function() {
	// executes when HTML-Document is loaded and DOM is ready
	// function btnClick(a){
	// 	alert("HHH")
	// }
	var now = new Date().getTime();
	// var now = 0;
	var endExamp = now + 1000*1*60
	// function coutDown(){
	// document.getElementsByClassName('mainQuestion')[0].style.display = 'block'
	$('.1').css('display','block')
	$('.btnPrev').click(function(){
		var checkQuesionNum = $('#inputIndex').val()
		if(checkQuesionNum == 1){
			$('.20').css('display','block')
			$('.1').css('display','none')
			$('#btnNum20').css('background-color','#138496')
			$('#btnNum20').css('color','white')			
			$('#btnNum1').css('background-color','white')
			$('#btnNum1').css('color','#138496')
			$('#inputIndex').val(20)

		}
		else{
			var tempClass = '.'+checkQuesionNum
			$(tempClass).css('display','none')
			var temClass4 = '#btnNum'+checkQuesionNum
			$(temClass4).css('background-color','white')
			$(temClass4).css('color','#138496')
			checkQuesionNum = Number(checkQuesionNum)-1
			var tempClass2 = '.'+checkQuesionNum
			$(tempClass2).css('display','block')
			var temClass3 = '#btnNum'+checkQuesionNum
			$(temClass3).css('background-color','#138496')
			$(temClass3).css('color','white')
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
		if(checkQuesionNum == 20){
			$('.20').css('display','none')
			$('.1').css('display','block')
			$('#btnNum1').css('background-color','#138496')
			$('#btnNum1').css('color','white')			
			$('#btnNum20').css('background-color','white')
			$('#btnNum20').css('color','#138496')
			$('#inputIndex').val(1)

		}
		else{
			var tempClass = '.'+checkQuesionNum
			$(tempClass).css('display','none')
			var temClass4 = '#btnNum'+checkQuesionNum
			$(temClass4).css('background-color','white')
			$(temClass4).css('color','#138496')
			checkQuesionNum = Number(checkQuesionNum)+1
			var tempClass2 = '.'+checkQuesionNum
			$(tempClass2).css('display','block')
			var temClass3 = '#btnNum'+checkQuesionNum
			$(temClass3).css('background-color','#138496')
			$(temClass3).css('color','white')
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
				$('#btnSubmit').click()
			}
		},1000)

});
