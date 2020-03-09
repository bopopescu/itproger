let array = [45, true, 35.23, "sfd", "s"];
//let str = array.join(",");
//console.log(str);


array[1] = false;
array[2] = "hello"
array[3] += " duk1e"


//console.log(array[2]);
console.log(array);

array[6] = 5
console.log(array);
//console.log("Длина массива: " + array.length);

array.pop()
array.push("Bob", "Alex", 55)
console.log(array);

array[array.length] = "Droid"
console.log(array);


array.shift();
console.log(array);


array.unshift(111, 222, 333);
console.log(array);

// Удаление обьектов
// array.length = 2
// console.log(array);

delete array[2];
console.log(array);

let arr = new Array(12, 213,"sm", true);
console.log(arr);

let arr2 = new Array(32)
console.log(arr2);

// Двумерный массив

let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8 ,9]
];
console.log(matrix);
console.log(matrix[1][1]);


matrix[0][4] = 45;
console.log(matrix);

// Трехмерный массива

let matrix2 = [
  [1 ,2 , [true, false]],
  [5, 4, 4]
]



let str = "Hello, world, 5, 0, 3.14"

let array_split = str.split(", ")
console.log(array_split);

console.log(array_split.splice(1,2));
