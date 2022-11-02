//====== modal1 ======
var modal = document.querySelector("#model1");
var trigger = document.querySelector("#trigger1");
var closeButton = document.querySelector("#close");

function toggleModal() {
    modal.classList.toggle("show-modall");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);


//====== modal2 ======
var modal2 = document.querySelector("#model2");
var trigger2 = document.querySelector("#trigger2");
var closeButton2 = document.querySelector("#close2");

function toggleModal2() {
    modal2.classList.toggle("show-modall");
}

function windowOnClick2(event) {
    if (event.target === modal2) {
        toggleModal2();
    }
}

trigger2.addEventListener("click", toggleModal2);
closeButton2.addEventListener("click", toggleModal2);
window.addEventListener("click", windowOnClick2);


//====== modal3 ======
var modal3 = document.querySelector("#model3");
var trigger3 = document.querySelector("#trigger3");
var closeButton3 = document.querySelector("#close3");

function toggleModal3() {
    modal3.classList.toggle("show-modall");
}

function windowOnClick3(event) {
    if (event.target === modal3) {
        toggleModal3();
    }
}

trigger3.addEventListener("click", toggleModal3);
closeButton3.addEventListener("click", toggleModal3);
window.addEventListener("click", windowOnClick3);