// let obj = '{"name": "Alex","age" : 45,"hasCar" : true}';
//
// obj = JSON.parse(obj);
//
// let array = '[56, 45, 2, 89]';
//
// array = JSON.parse(array);
//
// console.log(obj);
// console.log(obj.name);
//
// console.log(array[0]);
//

let obj2 = '{"name": "Alex", "state": "USA", "male": true, "frieds": [0,1,2,3]}';

obj2 = JSON.parse(obj2);

console.log(obj2.frieds[2]);


var object = {"name": "Alex", "state": 45, "male": true };


let str = JSON.stringify(object, "", 4);
console.log(str);
