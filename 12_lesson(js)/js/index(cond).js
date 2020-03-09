
let x = 20;
let y = 20;
let hasCar = false;



if (x > y) {
  console.log("Число х больше у");
  console.log("Проверка");
}
else if (x == y) {
  console.log("Числа равные");
  if (x != 24 || (hasCar==true && y == 24)) {  // && ||;   hasCar == true          == hasCar; hasCar == false  !hasCar
    console.log("Число х не равно 24");
  }
}
else if (x == 20) {
  console.log("Число 20");
}
else if (x == 26) {
  console.log("Число 26");
}
else {
  console.log("Числа не равные");
  console.log("Проверка");
}

let str = "Bob-1";
// Провека на конкретные значения
switch (str) {
  case "John":
    console.log("Имя John");
    break;
  case "George":
    console.log("Имя George");
    break;
  case "Petr":
    console.log("Имя Petr");
  case "Bob":
    console.log("Имя Bob");
    break;

  case "Bob-1":
  case "Bob-2":
    console.log("Имя Bob-1 или же Bob-2");
    break;
  default:
    console.log("Имя не найдено");
    break;
}

// Тернарный

let nums = 26;
let res = "";

if (nums > 25) {
  res = "Big";
}
else {
  res = "Small"
}

console.log(res);

let result =  nums > 25 ? "Big" : "Small"
console.log(result);


/*

==
!=
>
<
>=
<=

*/
