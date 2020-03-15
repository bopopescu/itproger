//task1
// $(document).bind("contextmenu",function(e){
//   return false;
// });
// Событие contextmenu вызывается при нажатии правой кнопкой мыши

//task2
alert($("#obj").removeClass("some"));

//task3
$(".btn").on("click",function(){
  $(".btn").hide();
});

//task4
$(".btn-2").on("click", function(){
  $(".p-btn-2").toggle();
});

//task5
$(".text").text("Текст был заменен");

//task6
console.log($(".last_link").attr("href"));

//task7
$(".btn-3").on("click", function(){
  $("#some_block").addClass("new_style");
});

//task8
$("#press-me").on("dblclick",function(){
  $("body").before("Двойной клик");
})
$("#press-me").on("mouseover",function(){
  $("body").before("Вы навели мышь");
})
$("#press-me").on("mouseout",function(){
  $("body").before("Вы убрали мышь");
})

//task9
$("p").bind("contextmenu", function(){
  return false;
})

// Работа с HTML!!!!!!!!
//taks1
var countChars = $("#rchars").text();
$("form > #textarea").on("keyup", function(){
  //console.log($(this).val());
  //console.log($(this).val().length);
  var charsLeft = countChars - $(this).val().length;
  if(charsLeft < 0){
    $("#rchars").text("0 символов осталось");
    $($(this).val($(this).val().substring(0,countChars)));
  }
  else
    $("#rchars").text(charsLeft + " символов осталось");
});
//------------------------------------------------------
// task2
$("#btn").on("click", function(){
  $("#a-for-del").removeAttr("href");
});
// task3
$("#disable-checkbox").on('click',function(){
  $(".disableCheck").prop("disabled",true);
});
//task4

$("#menuBtn").on("click", function(){
  var visibleMenu = $("#menu").is(":visible");
  //console.log(visibleMenu);
  if(visibleMenu){
    $("#menu").hide();
  }
  else{
    $("#menu").show();
  }
  //$("#menu").toggle();
})
// task5
$(document).ready(function(){
  $("head").append('<link rel="stylesheet" href="css/myStyle.css">')
});

//task6
//press-again
$("#press-again").bind("click", function(){
  $("#press-again").append("<p>«На надпись было нажато»</p>");
});
//task7
$(".print-link").on("click", function(){
  window.print();
  return false;
});
//task8
$(".p-pointer").each(function() {
  var obj = $(this)
  obj.text(obj.text() + ".");
});
//task9
var isOldTitle = true;

var oldTitle = "Програмирование";

var newTitle = " Cообщество itProger";

function changeTitle(){
  document.title = isOldTitle ? oldTitle : newTitle;
  isOldTitle = !isOldTitle;
}

setInterval(changeTitle, 700);

// Анимация
//taks1
$("#go-top").on("click",function(){
  $("html, body").animate({scrollTop:0},500);
})

//task2
//Мигающий текст
function blink_text(){
  $(".blink").fadeOut(500);
  $(".blink").fadeIn(500);
}

setInterval(blink_text, 1000);

//task3
$(document).scroll(function(){
  if($(document).width > 750){
    if($(document).scrollTop() > $('header').height() + 10)
    $('header').addClass("fixed");
    else {
      $('header').removeClass('fixed')
    }
  }
});

//task4
$(".task4").on('click', function(){
  $(this).slideUp(2000);
});

//task5
