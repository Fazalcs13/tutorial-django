// JavaScript Document

$(window).scroll(function() {
	$('header').each(function(){
	var imagePos = $(this).offset().top;
	var topOfWindow = $(window).scrollTop();
	
	 var wid= window.innerWidth;
	//alert(imagePos);
	console.log("topOfWindow "+topOfWindow);
	
		if (topOfWindow == 0)
		{
			//$(this).removeClass("fadeInDown hederFixedPos");
			
			/*$("#content1").removeClass("fadeInRight");
			$("#content1").addClass("displaynone");
			
			$("#contimg1").removeClass("fadeInLeft");
			$("#contimg1").addClass("displaynone");
			
			$("#content2").removeClass("fadeInLeft");
			$("#content2").addClass("displaynone");
			
			$("#contimg2").removeClass("fadeInRight");
			$("#contimg2").addClass("displaynone");*/
		}/*
		else if (topOfWindow > 768)
		{
			$(this).removeClass("fadeInDown hederFixedPos");
		}*/
		else
		{
			//$(this).addClass("fadeInDown hederFixedPos");
		}
		
		/*if(topOfWindow >= 300)
		{
			$("#content1").addClass("fadeInRight");
			$("#content1").removeClass("displaynone");
			
			$("#contimg1").addClass("fadeInLeft");
			$("#contimg1").removeClass("displaynone");
			
			$("#pastcont1").addClass("fadeInLeft");
			$("#pastcont2").addClass("fadeInDown");
			$("#pastcont3").addClass("fadeInRight");
			
		}
		
		if(topOfWindow >= 700)
		{
			$("#content2").addClass("fadeInLeft");
			$("#content2").removeClass("displaynone");
			
			$("#contimg2").addClass("fadeInRight");
			$("#contimg2").removeClass("displaynone");
			
			$("#pastcont4").addClass("fadeInLeft");
			$("#pastcont5").addClass("fadeInDown");
			$("#pastcont6").addClass("fadeInRight");
			$("#pastcont7").addClass("fadeInLeft");
			$("#pastcont8").addClass("fadeInRight");
		}
		
		if(topOfWindow >= 1400)
		{
			$("#content3").addClass("fadeInRight");
			$("#content3").removeClass("displaynone");
			
			$("#contimg3").addClass("fadeInLeft");
			$("#contimg3").removeClass("displaynone");
			
			
		}
		
		if(wid <=870)
		{
		}*/
	});
});

$(window).resize(function() {
   var width = $(this).width();
  
   if(width<768)
   {
	   $('#collapseTwo').removeClass("collapse in");
	   $('#collapseTwo').addClass("collapse");
	   $('#chngeicon').addClass("fa-caret-down");
		$('#chngeicon').removeClass("fa-caret-up");
   }
   else
   {
	   $('#collapseTwo').addClass("collapse in");
	   $('#collapseTwo').removeClass("collapse");
	}
});


$(window).load(function() {
   var width = $(this).width();
  
   if(width<768)
   {//alert();
	   $('#collapseTwo').removeClass("collapse in");
	   $('#collapseTwo').addClass("collapse");
	   $('#chngeicon').addClass("fa-caret-down");
		$('#chngeicon').removeClass("fa-caret-up");
   }
   else
   {
	   $('#collapseTwo').addClass("collapse in");
	   $('#collapseTwo').removeClass("collapse");
	}
});



function chngeMenuIcon()
{
	if($('#chngeicon').hasClass("fa-caret-down"))
	{
		$('#chngeicon').removeClass("fa-caret-down");
		$('#chngeicon').addClass("fa-caret-up");
	}
	else
	{
		$('#chngeicon').addClass("fa-caret-down");
		$('#chngeicon').removeClass("fa-caret-up");
	}
}







