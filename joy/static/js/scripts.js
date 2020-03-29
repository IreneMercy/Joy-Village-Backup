$(document).ready(function(){
	$('.menu').click(function(){
		$('.toggle').toggleClass('active');
	})

	$('#contactform').submit(function(e){
		var name = document.getElementById('#name'),
		    email = document.getElementById('#email'),
		 		message = document.getElementById('#message');
		if (name.value==''|| !email.value || !message.value){
				alertify.error('Please fill all fields')
		}
		else{
			$.ajax({
				url:"http://formsfree.io/"
			})
			e.preventDefault()
			$(this).get(0).reset()
			alertify.succsess('Message sent')
		}
	})
})
