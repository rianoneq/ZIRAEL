const burger = document.getElementById('burger');
const navLinks = document.querySelector('.nav_links');

burger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
})

// const menuBtn = document.querySelector('.menu-btn');
let menuOpen = false;
burger.addEventListener('click', ()=> {
    if(!menuOpen) {
        burger.classList.add('open');
        menuOpen=true;
    }
    else {
        burger.classList.remove('open');
        menuOpen=false;
    }
})
