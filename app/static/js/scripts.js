// document.addEventListener("DOMContentLoaded", function () {
//   const imageIds = [66, 177, 390, 478, 509, 525, 543, 564, 646, 653, 654, 773, 777, 791,
//                     871, 901, 903, 1015, 1018, 1022, 1035, 1036, 1039,
//                     1044, 1056];
//   let currentIndex = 0;

//   function switchImage() {
//     const trekkingImage = document.getElementById('trekkingImage');
//     const nextImageId = imageIds[currentIndex];
//     trekkingImage.src = `https://picsum.photos/id/${nextImageId}/800/600`;

//     // Move para a próxima imagem ou volta ao início
//     currentIndex = (currentIndex + 1) % imageIds.length;
//   }

//   // Inicia o alternador de imagens a cada 1 minuto (60000 ms)
//   setInterval(switchImage, 15000);
// });

document.addEventListener("DOMContentLoaded", function () {
  const imageIds = [66, 177, 390, 478, 509, 525, 543, 564, 646, 653, 654, 773, 777, 791,
                    871, 901, 903, 1015, 1018, 1022, 1035, 1036, 1039,1044, 1056]

  function fillCarousel() {
    carousel = document.getElementById('corouselImages')

    carousel.innerHTML = `<div class="carousel-item active">
      <img src="https://picsum.photos/id/66/800/600" class="d-block w-100" alt="Imagem 66">
      </div>`

    for (let i = 1; i < imageIds.length; i++) {
      carousel.innerHTML += `<div class="carousel-item">
        <img src="https://picsum.photos/id/${imageIds[i]}/800/600" class="d-block w-100" alt="Picsum Photo ${imageIds[i]}">
      </div>`
    }
  }

  fillCarousel()
})