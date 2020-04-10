$(document).ready(function(){

	$('#contactform').on('submit',function(event){
		event.preventDefault()
		console.log('success')
		form = $("#contactform")

		$.ajax({
			url:'/contact',
			type:'POST',
			data:form.serialize(),
			dataType:'json',
			success: function(response){
				$('#alert').html(response);
				// alert(data['success'])
			},

		})
		$('#id_from_email').val(''),
		$('#div_id_subject').val(''),
		$('#div_id_message').val(''),
		$('input[name=csrfmiddlewaretoken]').val()

	})

	$('.form').submit(function(event){
		event.preventDefault()
		form = $(".form")
		$.ajax({
			url:'',
			type:'POST',
			data:form.serialize(),
			dataType:'json',
			success: function(data){
				alert(data['success'])
			},

		})
		$('#id_from_email').val(''),
		$('#div_id_subject').val(''),
		$('#div_id_message').val(''),
		$('input[name=csrfmiddlewaretoken]').val()

	})

	$('.form').submit(function(event){
		event.preventDefault()
		form = $(".myform")
		$.ajax({
			url:'',
			type:'POST',
			data:form.serialize(),
			dataType:'json',
			success: function(data){
				alert(data['success'])
			},

		})
		$('#id_from_email').val(''),
		$('#div_id_subject').val(''),
		$('#div_id_message').val(''),
		$('input[name=csrfmiddlewaretoken]').val()

	})

	$('#myform').submit(function(event){
		event.preventDefault()
		form = $(".myform")
		$.ajax({
			url:'',
			type:'POST',
			data:form.serialize(),
			dataType:'json',
			success: function(data){
				alert(data['success'])
			},

		})
		$('#id_from_email').val(''),
		$('#div_id_subject').val(''),
		$('#div_id_message').val(''),
		$('input[name=csrfmiddlewaretoken]').val()

	})

	$('.menu').click(function(){
		$('.toggle').toggleClass('active');
	})

});
