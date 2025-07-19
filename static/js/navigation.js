const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.main-nav');

let menuOpen = false;

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
  menuOpen = !menuOpen;
});
