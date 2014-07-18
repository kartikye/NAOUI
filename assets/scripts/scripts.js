$(document).ready(function() {
	$('#volume').slider();


});

//Check for Data on Socket
	function readSocket(){
		$.post('../../php/readSocket.php', id = "h", function(data) {
			console.log(data);
		});
		setTimeout(readSocket(), 30000);
	}

//Volume
	$('#volume').on('slideStop', function(event){
		var volume =  $('#volume').slider('getValue');
		$.post('../../php/functions.php', {id: "vol", content: volume}, function(data) {
		});
	});

//IP
	$('#setIP').on('click', function() {
		console.log('hello');
		var ip = $('IPText').value;
		console.log(ip);
		$.post('../../php/functions.php', {id: "ipa", content: ip}, function(data) {
			if (data == "proxcon") {
				alert("Proxy Connected");
			}else{

			}
		});
	});

//Stiffness
	$('#stiffOn').on('click', function() {
		$.post('../../php/functions.php', id = "son", function(data) {
			console.log(data);
			console.log('done');
		}).done(function(){
			console.log('done');	
		})
		;
	});

	$('#stiffOff').on('click', function() {
		$.post('../../php/functions.php', id = "sof", function(data) {
		});
	});

