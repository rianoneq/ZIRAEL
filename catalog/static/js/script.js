let card_description = document.querySelectorAll('.product_descr')
let card_name = document.querySelectorAll('.product_name')

card_description.forEach(text => {
  let max_length = 0
  if (window.innerWidth < 320) {
    card_description.remove;
  }
  if (window.innerWidth < 550) {
    max_length = 10
  }
  else if (window.innerWidth < 600) {
    max_length = 20
  }
  else if (window.innerWidth < 1000) {
    max_length = 25
  }
  else if (window.innerWidth < 1200) {
    max_length = 50
  }
  else if (window.innerWidth < 1400) {
    max_length = 85
  }
  else if (window.innerWidth < 1800) {
    max_length = 100
  }
  else if (window.innerWidth > 1800) {
    max_length = 125
  }
  
  //console.log(max_length)
  if (text.innerHTML.length > max_length) {
    let cutten_text = text.innerHTML.trim().slice(0,[max_length]);
    console.log(cutten_text)
    text.innerHTML = cutten_text + '...';
  }
});

