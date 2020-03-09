function clickHref(){
  alert("Hello all");
  document.querySelector('a.href').style.color="#333";
  document.querySelector('a.href').style.textDecoration = 'none';

}

function clickText (selector) {
  document.querySelector(selector).style.backgroundColor = '#333';
  document.querySelector(selector).style.color = 'white';
}

let input = document.querySelector('input');

function focusEvent() {
  input.style.backgroundColor = "#333";
  input.style.padding = "10px";
  input.style.border = "0";

}

function focusEndEvent() {
  input.style.backgroundColor = "#fff";
  input.style.border = "1px solid silver";
  input.style.padding = "0px";
}


input.onmouseover = function() {
  console.log('onmouseover');
};

window.onresize = function() {
  console.log("Ширина  = " + window.innerWidth);
  console.log("Высота  = " + window.innerHeight);
};

window.onload = function() {
  console.log("Страница загрузилась");
};
window.onscroll = function() {
    console.log("Скролл мышкой");
};

let textArea = document.querySelector('.full-text');

textArea.oninput = function() {
  console.log("нажата кнопка");
};

//--------------Обработчики событий-----------------
let block = document.querySelector("div.block");

function handlerOver() {
  block.innerHTML = "Новый текст";
}

function handlerOut() {
  block.innerHTML = "Привет мир";
};

block.addEventListener("mouseover", handlerOver);
block.addEventListener("mouseout", handlerOut);


block.removeEventListener("mouseout", handlerOut);
