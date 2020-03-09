console.log("hello");

let text = document.querySelector(".full-text");

text.onkeydown = function(e) {
  console.log("onkeydown: " + text.value);
};

text.onkeypress = function(e) {
  console.log("onkeypress: " + text.value);
};

text.onkeyup = function(e) {
  console.log("onkeyup: " + text.value);
};

let boldText = document.querySelector("p > b.bold-txt");

boldText.onmousedown = function(){
  boldText.style.color = "red";
}

boldText.onmouseup = function(){
  boldText.style.color = "blue";
}

boldText.oncontextmenu = function(){
  boldText.style.color = "green";
}


let inputField = document.querySelector(".input");
let helpField = document.querySelector(".hint");

inputField.onmouseenter = function() {
  helpField.style.display = "block";
};

inputField.onmouseleave = function() {
  helpField.style.display = "none";
};

inputField.onmousemove = function(e) {
  helpField.style.left = e.pageX + "px";
  helpField.style.top = e.pageY + "px";
};
