$(document).ready(function (e) {
	$("#uploadimage").on('submit',(function(e) {
		e.preventDefault();

		var fd = new FormData();
        var files = $('#file')[0].files[0];
        fd.append('file',files);

		$.ajax({
			url: "/predict/", // Url to which the request is send
			type: "POST",             // Type of request to be send, called as method
			data: fd, // Data sent to server, a set of key/value pairs (i.e. form fields and values)
			contentType: false,       // The content type used when sending data to the server.
			cache: false,             // To unable request pages to be cached
			processData:false,        // To send DOMDocument or non processed data file it is set to false
			
			success: function(data)   // A function to be called if request succeeds
			{
				$('.well p').text('Predicted Output: ' + data.result);
			},
			error: function(xhr, ajaxOptions, thrownError)
			{
		        $('.well p').text('[ERROR] ' + xhr.status + ' / ' + thrownError);
	      	}
		});
	}));

	// Function to preview image after validation
	$(function() {
		$("#file").change(function() {
			
			var file = this.files[0];
			var imagefile = file.type;
			var match= ["image/jpeg","image/png","image/jpg"];
			if(!((imagefile==match[0]) || (imagefile==match[1]) || (imagefile==match[2])))
			{
				$('#previewing').attr('src','noimage.png');
				alert('wrong image format');
				return false;
			}
			else
			{
				var reader = new FileReader();
				reader.onload = imageIsLoaded;
				reader.readAsDataURL(this.files[0]);
			}
		});
	});
	function imageIsLoaded(e) {
		$("#file").css("color","green");
		$('#image_preview').css("display", "block");
		$('#previewing').attr('src', e.target.result);
		$('#previewing').attr('width', '250px');
		$('#previewing').attr('height', '230px');
	};
});