var i = 0


function Show (){
  var el = "Element"
  console.log(el);
  console.log(i);
}

function calc(a, b = 10){
  // if (b == undefined) {
  //   b = 10;
  // }
  var res = a + b;
  console.log(res);
}

// // let func = calc;
// func(5,10);
// func = null;

let func = function(mess = "Bob"){
  console.log("Привет: " + mess);
};
func();
func("Alex");


function multiply(a, b, c){
  var res = a * b * c;
  return res;
}

Show();
calc(56);
calc(56, 6);


let  x = multiply(2, 4, 8)
console.log(x);

function arrayEven(array){
  let isEven = true;
  array.forEach((item, i) => {
    if (item % 2 != 0){
      isEven = false;
    }
  });
  return isEven;
}

let arr = [5, 9, 0 ,4];
let arr2 = [6, 8, 0 ,4];

let isEven = arrayEven(arr2);
console.log(isEven);

function test(words) {
  console.log(words);
}

setTimeout(test, 1500, "Hello world");

setTimeout("console.log('Hello')", 1500);

let timeOut  = setTimeout(function(){
  console.log("asdasdasdasdsadasdsadasdas");
}, 1500)

clearTimeout(timeOut);

let interval = setInterval(function(){
  console.log("asdasdasdasdsadasdsadasdas");
}, 2000)

setTimeout(function(){
  clearInterval(interval);
  console.log("Stop");
},5000);

//setInterval(test, 2000, "setInterval");
