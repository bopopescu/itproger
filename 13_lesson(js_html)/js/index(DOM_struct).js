// console.log(document.documentElement);
// console.log(document.body);
// console.log(document.head);
//
//
// console.log(document.body.childNodes);
//
// for(var i = 0; i < document.body.childNodes.length; i++) {
//   console.log(document.body.childNodes[i]);
// }
// for (var item in document.body.childNodes) {
//   if (document.body.childNodes.hasOwnProperty(item)) {
//     console.log(item);
//   }
// }
//let content = document.getElementById("content");
//let elements = content.getElementsByTagName("*")[0];

//console.log(elements);
// for (var i = 0; i < elements.length; i++) {
//   console.log(elements[i]);
// }
//
// console.log(content);
//
// let el = document.getElementsByName("fname")[0].tagName;
// console.log(el);
//
//
// let allClasses = document.getElementsByClassName("some");
// console.log(allClasses.length);
//
// let elements = document.querySelector("#content");
// console.log(elements);

//let ulItems = document.querySelector("#span-text");

let ulItems = document.querySelectorAll("#span-text")[0];

let parentLi = ulItems.closest(".some-text");

parentLi.innerHTML = " Новое значение";


let input = document.querySelector('input[type]');
console.log(input.value);


if (input != null) {
  input.value = " фыафыафыа";

  input.setAttribute("data-toggle","some-value");
  input.setAttribute("type","text");

  if (input.hasAttribute("type")) {
    alert(input.getAttribute("class"));

  };

  input.className = "some new test";
  alert(input.className)
  //input.removeAttribute("class");
}

//document.write("HTML");

input.style.backgroundColor = "red";
input.style.color = "#fff";
input.style.border = "2px solid silver";
input.style.borderRadius = "5px";
input.style.padding = "12px 15px";
