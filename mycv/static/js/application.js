$(document).ready(function(){
  $('body').append('<div class="overlay"></div>');
  overlay = $('.overlay');
  overlay.css('opacity','.8');
  $(".welcome").css('display','block');
  
  $(".welcome .close").click(function(){
    $(this).parent().parent().css('display','none');
    overlay.remove();
  });
  
  $('a[rel*=external]').click(function(e) {
    window.open(this.href);
    return false;
  });  
    
});
