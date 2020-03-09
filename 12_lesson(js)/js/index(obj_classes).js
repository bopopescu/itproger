// let speed = 45;
// let fuel = 60;
//
// let car = [45, 23, 4]
let car = {
  marka : "Volvo",
  speed : 60,
  type: "sedan",
  fuel: 50,
  passengers: ["Alex", "Bob"],
  isNew: true
};

console.log(car["speed"]);

for (var item in car)
    //console.log(item);
    console.log("Элемент по ключу " + item + ": " + car[item]);

for (var item2 in car) {
  if (car.hasOwnProperty(item2)) {
    console.log(item2);
  }
}

// function Car(marka,color, type, speed) {
//   this.marka = marka;
//   this.color = color;
//   this.type = type;
//   this.speed = speed;
// }

class Car {
  constructor(marka, color, type, speed) {
    this.marka = marka;
    this.color = color;
    this.type = type;
    this.speed = speed;
  }

  info(){
    console.log("Marka: " + this.marka + "Color: " + this.color + "Type: " + this.type + "Speed: " + this.speed);
  }
}

let bmw = new Car("M3", "Blue","Sedan", 270);
console.log(bmw.speed);
bmw.color = "Красный";
console.log(bmw.color);
bmw.info();
bmw.weight = 1200;
console.log(bmw.weight);
//-------------------------------------------------------------------------------------------------------------
let volvo = new Car("M3", "White","Sedan", 270);
console.log(volvo.color);
volvo.info();

let arr = new Array(45,45);
console.log(arr[1]);
