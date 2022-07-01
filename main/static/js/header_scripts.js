const burger = document.getElementById('burger');
const navLinks = document.querySelector('.nav_links');
let meAccount = document.querySelector('.me_account');

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

let max_length = 0
if (window.innerWidth < 550) {
    max_length = 14
}

else if (window.innerWidth < 1200) {
    max_length = 10
}

else if (window.innerWidth > 1800) {
    max_length = 10
}
if (meAccount.innerHTML.trim().length > max_length) {
    
    meAccount.innerHTML = meAccount.innerHTML.trim().slice(0,[max_length]).trim() + '...';
}
