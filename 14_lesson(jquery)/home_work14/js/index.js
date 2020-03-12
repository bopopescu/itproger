var task = [];
var taskCount = 0;
var userInput = "";

//Получаем ввод от пользователя
$("input").on("keyup", function() {
  userInput = $(this).val();
});

//Действия при нажатии "Добавить"
$(".button-add").on("click", function() {
  if(userInput.length > 0 && userInput != ''){
    taskCount++;
    task.push("Задание #" + taskCount + ": " + userInput);
    $('input').val("");
    userInput = "";
    $("#addTask > p").css("display","block");

    setTimeout(function(){
      $("#addTask > p").css("display","none");
    },1500);
  }
  else
    return false;
});

//Действия при нажатии "Отобразить"
$(".button-show").on("click",function() {
  if(task.length > 0){
    $("#show-task").empty();
    for (var i = 0; i < task.length; i++) {
      $("#show-task").append("<p>" + task[i] + "</p>");
    }
  }
});
