// // ---------Task1------------------
let number = 5;

function getNumber(){
  let start = true;

  do {
    userNumber = prompt("Задание №1. Введите число: ");
    if(userNumber == number)
      start = false;
  } while (start);

  alert("Поздравляем!Вы ввели верное число!")
}
getNumber();

// ---------Task2------------------
window.onresize = function (){
  alert("Вы узменили ширину или высоту экрана!" + '\n' + "Ширина: " + window.innerWidth + "px" +  '\n' + "Высота: " + window.innerHeight + "px")
  console.log("Ширина: " + window.innerWidth);
  console.log("Высота: " + window.innerHeight);
}

// ---------Task3------------------
let boldText = document.getElementsByTagName('b');
//console.log(boldText);

let pText = document.querySelector('.p-text');

pText.onmouseover = function () {
  for (var i = 0; i < boldText.length; i++) {
    boldText[i].style.color = "red";
  }
}
pText.onmouseout = function () {
  for (var i = 0; i < boldText.length; i++) {
    boldText[i].style.color = "black";
  }
}

// ---------Task4------------------
function getAttributes(){
  let hrefLink = document.querySelector("a");
  alert("Атрибуты ссылки:" + '\n' + "href = " + hrefLink.href + '\n' +
  "hreflang = " + hrefLink.hreflang + '\n' +
  "rel = " + hrefLink.rel + '\n' +
  "target = " + hrefLink.target + '\n' +
  "type = " + hrefLink.type);
}
