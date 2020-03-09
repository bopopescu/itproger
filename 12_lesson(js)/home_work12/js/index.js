//task1
function sumArray(array){
  let sum = 0;
  for (var i = 0; i < array.length; i++) { // 1000
    if (array[i] % 3 == 0  || array[i] % 5 == 0){
      sum += array[i];
    }
  }
  return sum;
}
function sumArray2(){
  let sum = 0;
  for (var i = 0; i < 1000; i++) { // 1000
    if (i % 3 == 0  || i % 5 == 0){
      sum += i;
    }
  }
  return sum;
}



let array = [12, 14, 15, 45, 13, 16];
console.log(array);
console.log("Сумма всех чисел кратных 3 или 5 = " + sumArray(array));
console.log("Сумма всех чисел кратных 3 или 5 до 1000 = " + sumArray2());

// task 2
function  minInArray(array){
  var min = array[0][0];
  for (var i = 0; i < array.length; i++) {
    for (var j = 0; j < array.length; j++) {
      if (min > array[i][j]){
        min = array[i][j];
      }
    }
  }
  return min;
}

var x = new Array(new Array(20, 34, 2), new Array(9, 12, 18), new Array(3, 4, 5));
console.log(x);
var minimum = minInArray(x);
console.log("Минимальное число из массива: " + minimum);
