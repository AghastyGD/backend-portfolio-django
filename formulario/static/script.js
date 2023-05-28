// Espera até que todo o DOM seja carregado
$(document).ready(function() {

  // Adiciona a classe 'sticky' à navbar quando a página é rolada para baixo
  $(window).scroll(function() {
    if (this.scrollY > 20) {
      $('.navbar').addClass('sticky');
    } else {
      $('.navbar').removeClass('sticky');
    }
    
    // Adiciona a classe 'show' ao botão de scroll-up-btn quando a página é rolada 500 pixels para baixo
    if (this.scrollY > 500) {
      $('.scroll-up-btn').addClass('show');
    } else {
      $('.scroll-up-btn').removeClass('show');
    }
  });

  // Script de deslize para cima
  $('.scroll-up-btn').click(function() {
    $('html').animate({scrollTop: 0});
  });

  // Script de animação de digitação
  var typed = new Typed('.typing', {
    strings: ['Desenvolvedor Python', 'Editor', 'Blogueiro', 'Designer Gráfico', 'Desenvolvedor Web', 'Youtuber', 'Freelancer'],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
  });

  // Script de alternância do menu/navbar
  $('.menu-btn').click(function() {
    $('.navbar .menu').toggleClass('active');
    $('.menu-btn i').toggleClass('active');
    return false;
  });

  // Script de fechamento automático do menu/navbar quando um link é clicado
  const menuLinks = document.querySelectorAll('.menu-link');
  menuLinks.forEach(link => {
    link.addEventListener('click', () => {
      const menuToggle = document.querySelector('.menu-btn');
      const navbarMenu = document.querySelector('.navbar .menu');
      const menuBtnIcon = document.querySelector('.menu-btn i');
      
      // Define a propriedade 'checked' do menuToggle para 'false'
      menuToggle.checked = false;
      
      // Remove a classe 'active' da navbarMenu e do menuBtnIcon
      navbarMenu.classList.remove('active');
      menuBtnIcon.classList.remove('active');
    });
  });

});
