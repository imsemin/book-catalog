const navToggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.menu');

navToggle.addEventListener('click', function() {
    links.classList.toggle('show-menu')
})