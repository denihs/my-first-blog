$(function() {
  $('.toggleNav').on('click',function() {
    $('.cabecalho-pagina h1').toggleClass('open');
  });
  $('.saudacao').on('click',function() {
    $('.toggleNav').toggleClass('close');
  });


});
