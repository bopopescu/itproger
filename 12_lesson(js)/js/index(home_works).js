console.log("HEllo");

//циклы
// -----------------------------------------------------------------------
// var num = 13;
//
// var str = "";
//
// while (num > 0) {
//   if (num == 10) {
//     num--;
//     continue;
//   }
//   else{
//     if (num != 1)
//     {
//       str += num + ", ";
//       num--;
//     }
//     else
//     {
//       str += num;
//     }
//   }
// }
// console.log(str);

//--------------------------------------------------------------------
//var sum = 0;

// for (var i = 0; i < 100; i++) {
//   if(i % 4 == 0){
//     sum += i;
//   }
// }
// console.log(sum);
//-------------------------------------
// var num = prompt("Enter the number");
// count_chet = 0;
// count_nechet = 0;
// for (var i = 0; i < num.length; i++) {
//   if(num[i] % 2 == 0){
//     count_chet++;
//   }
//   else{
//     count_nechet++;
//   }
// }
// console.log("Четных чисел = " + count_chet + ", " + "Нечетных чисел = " + count_nechet);

//
// //1
// let arr = ["Иван",35, true];
// console.log(arr);
// //2
// var today = new Date();
//
// var day = today.getDate();
// var month = today.getMonth() + 1;
// var year = today.getFullYear();
// if (day < 10){
//   day = "0" + day;
// }
//
// today = month + "-" + day + "-" + year;
//
// console.log(today);
//
// //2
// console.log(document.URL);
//
// //3
//
// var number = prompt("Введите число с 4 цифрами: ")
//
// var n1 = Math.floor(number / 1000 % 10);
//
// var n2 = Math.floor(number / 100 % 10);
//
// var n3 = Math.floor(number / 10 % 10);
//
// var n4 = Math.floor(number % 10);
//
// console.log(n1 + ", " + n2 + ", " + n3 + ", " + n4 + ", ");
//
//
// //4
// var num = prompt("Введите число : ");
// var num1 =  parseInt(num);
// var num2 = parseInt(num * 2);
//
// console.log(num1.toString() + num2.toString());
//
//
// //5
// var n = 46;
// var str = "string";
// console.log(n * 5);
// console.log(str);
//
// //6
// var url = prompt("Введите имя адреса сайта: ");
// var domen = url.split(".");
// console.log(domen[1]);
// //7
// let a = 5;
// let b = "F";
// let c = "Привет";
// let d = 90.2;
// const MY_CONST = 67;
//
// console.log(c);














// function sumArray(array){
//   let sum = 0;
//   for (var i = 0; i < array.length; i++) { // 1000
//     if (array[i] % 3 || 0  && array[i] % 5 == 0){
//       sum += array[i];
//     }
//   }
//   return sum;
// }
//
//
//
// let array = [12, 14, 15, 45, 13, 16]
// console.log("Сумма всех чисел кратный 3 или 5 = " + sumArray(array));
