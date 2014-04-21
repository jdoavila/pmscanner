$( "#txtBarCode" ).keypress(function(e) {
	if(e.which == 13){
		//alert(e.which);
		$("#pbPrincipal").css("display", "block");
		q = $("#txtBarCode").val();
		$.ajax({
			url: '/getprice/',
			type: 'GET',
			data: {
				'q': q
			},
			traditional: true,
			dataType: 'html',
			success: function(result) {
				$("#resultado").remove();
				$('#nuevosdatos').append(result);
				//alert(result);
				$("#pbPrincipal").css("display", "none");
				$("#txtBarCode").val("");
				$("#txtBarCode").focus();
			}
		});
	}
  	console.log(e.which);
});