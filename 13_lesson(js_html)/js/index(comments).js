let btnForm = document.querySelector("#comments-form button");
let countComments = 0;
let idComment =0;

btnForm.onclick = function() {
  idComment++;

  let form = document.querySelector("#comments-form");
  if(form.name.value.length < 4){
    document.querySelector("#error").innerHTML = "Длина имени не менее 4 символов";
    return false;
  }
  else if(form.comment.value.length < 12){
    document.querySelector("#error").innerHTML = "Длина длина сообщения не менее 10 символов";
    return false;
  }

  document.querySelector("#error").innerHTML = "";

  //Установим новое значени для подсчета коментариев
  if(countComments == 0){
    document.querySelector("#comments").innerHTML = "";
  }

  countComments++;
  document.querySelector(".count-comm").innerHTML = countComments;

  let newComment = "<div class='comment' id='block-"+ idComment +"'>" +
    "<span class='delete' onclick='delComm(" + idComment +")'>&times</span>" +
    "<p class='name'>" + form.name.value + "</p>" +
    "<p class='mess'>" + form.comment.value + "</p>" +
  "</div>";

  document.querySelector("#comments").insertAdjacentHTML('afterbegin', newComment); //beforeend

  //очистка формы

  form.comment.value = "";
};


function delComm(id){
  document.querySelector("#block-" + id).remove();

  countComments--;

  document.querySelector(".count-comm").innerHTML = countComments;

  if(countComments == 0){
    document.querySelector("#comments").innerHTML = "Пока коментариев нет";
  }
}
