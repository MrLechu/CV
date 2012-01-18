$(document).ready(function(){
  $('body').append('<div class="overlay"></div>');
  overlay = $('.overlay');
  overlay.css('opacity','.6');
  
  $(".welcome .close").click(function(){
    $(this).parent().css('display','none');
    overlay.remove();
  })
    
});
