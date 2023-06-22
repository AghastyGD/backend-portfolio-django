document.addEventListener("DOMContentLoaded", function() {
    var slideshow = document.querySelector(".slideshow");
    var images = slideshow.getElementsByTagName("img");
    var currentImageIndex = 0;

    function showNextImage() {
        images[currentImageIndex].classList.remove("active");
        currentImageIndex = (currentImageIndex + 1) % images.length;
        images[currentImageIndex].classList.add("active");
    }

    // Mostrar a primeira imagem inicialmente
    images[currentImageIndex].classList.add("active");

    // Trocar a imagem a cada 5s
    setInterval(showNextImage, 5000);
})