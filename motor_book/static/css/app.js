const navToggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.menu');

navToggle.addEventListener('click', function() {
    links.classList.toggle('show-menu')
})

const modalBtn = document.querySelector('.modal-btn');
const modalOverlay = document.querySelector('.order-overlay');
const closeBtn = document.querySelector('.close-btn');

modalBtn.addEventListener('click', function() {
    modalOverlay.classList.add('open-modal')
})

closeBtn.addEventListener('click', function() {
    modalOverlay.classList.remove('open-modal')
})