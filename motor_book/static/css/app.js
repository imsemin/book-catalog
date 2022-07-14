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

var phoneMask = IMask(
    document.getElementById('id_phone_number'), {
        mask: '{7}-000-000-00-00'
});

document.getElementById('id_buyer_name').placeholder = 'Имя';
document.getElementById('id_buyer_surname').placeholder = 'Фамилия';
document.getElementById('id_phone_number').placeholder = 'Номер телефона';
document.getElementById('id_email').placeholder = 'Email';
document.getElementById('id_comment').placeholder = 'Комментарий';
