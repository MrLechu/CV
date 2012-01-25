$(document).ready(function(){
  // $('body').append('<div class="overlay"></div>');
  // overlay = $('.overlay');
  // overlay.css('opacity','.8');
  // $(".welcome").css('display','block');
//   
  // $(".welcome .close").click(function(){
    // $(this).parent().parent().css('display','none');
    // overlay.remove();
  // });
  
  $('a[rel*=external]').click(function(e) {
    window.open(this.href);
    return false;
  });  


  var ajaxLoader = $("#ajax-loader");

  
  $("#bookmark").toggle(function(){
    $(ajaxLoader).css('display','block');
    $("#smenu").slideDown("slow",function() {ajaxLoader.css('display','none')});
    $(this).animate({top: '+=130'}, 'slow', function(){$(this).css('display','block')});
    
  }, function(){
     $(ajaxLoader).css('display','block');
     $("#smenu").slideUp("slow",function() {$(ajaxLoader).css('display','none')});
     $(this).animate({top: '-=130'}, 'slow', function(){$(this).css('display','block')});
   });  
});