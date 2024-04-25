// ----- Nav bar menu opening -----//

const nav_menu = document.getElementById("nav-menu");
const menu_show_button = document.getElementById("nav-toggle");
const menu_hide_button = document.getElementById("menu_hide_btn");
const show_menu = "show_menu";

menu_show_button.addEventListener("click", funShow);
menu_hide_button.addEventListener("click", funHide);

function funShow() {
    nav_menu.classList.add(show_menu);
}

function funHide() {
    nav_menu.classList.remove(show_menu);
}

//----- active menu li a -----//
// Get all sections that have an ID defined 
const sections = document.getElementsByTagName("section[id]");
//add an event listener listening for scroll 
window.addEventListener("scroll", navHighlighter);
function navHighlighter() {
    //Get current scroll position
    let scrollY = window.pageYOffset;

    // now we loop thru sections to get height, top and id valuers for each 
    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 50;
        sectionID = current.getAttribute("id");

        /*
        -if out current schroll position enters the space where current section on screen is, add
        - To know which link needs an active class, we ise sectionId variable we are getting while
        */
       if(
        (scrollY >= sectionTop) &&
        (scrollY <= sectionTop + sectionHeight)
        ) {
            document.querySelector(`.nav__menu a[href*=" + sectionID + "]`).classList.add("active-link");
        } else {
            document.querySelector(`.nav__menu a[href*=" + sectionID + "]`).classList.remove("active-link");
        }
    });
};

//----Sliders---//
var swiper = new Swiper(".slide-content", {
    slidesPerView: 1, 
    spaceBetween: 40,
    effect: "coverflow",
    grabCursor: true, 
    centeredSlides: true, 
    loop: true, 
    centerSlide: 'true', 
    fade: 'true', 
    pagination: {
        el: ".swiper-pagination",
        clickable: true, 
    },
    coverflowEffect: {
        rotate: 0, 
        stretch: -40,
        depth: 80, 
        modifier: 1, 
        sliderShade: false, 
    }, 
    breakpoints:{
        280: {
            sliderPerView: 1,
            spaceBetween: 10,
        },
        410: {
            sliderPerView: 1.1,
            spaceBetween: 20,
            coverflowEffect:
            {
                stretch: -20,
            }
        },
        768: {
            sliderPerView: 2,
            spaceBetween: 20,
            coverflowEffect:
            {
                stretch: -420,
            }
        },
        1024: {
            sliderPerView: 3,
            spaceBetween: 30,
            coverflowEffect:
            {
                stretch: -30,
            }
        },
    }
});

//---- parallex effect ---//
var scene = document.getElementById('scene');
var parallex = new Parallax(scene);

var scene = document.getElementById('scene2');
var parallex = new Parallax(scene2);

var scene = document.getElementById('scene3');
var parallex = new Parallax(scene3);

var scene = document.getElementById('scene4');
var parallex = new Parallax(scene4);

//-- animation ---//
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 200,
    reset: true,
});
//bottom
sr.reveal('.sr01', {delay: 300, origin: 'bottom' }), 
    sr.reveal('.sr02', {delay: 600, origin: 'bottom' }),
    sr.reveal('.sr03', {delay: 900, origin: 'bottom' }),
    sr.reveal('.sr04', {delay: 1200, origin: 'bottom' }),
    sr.reveal('.sr05', {delay: 1500, origin: 'bottom' });
//top
sr.reveal('.sr06', {delay: 300, origin: 'top' }),
    sr.reveal('.sr07', {delay: 600, origin: 'top' }),
    sr.reveal('.sr08', {delay: 900, origin: 'top' }),
    sr.reveal('.sr09', {delay: 1200, origin: 'top' }),
    sr.reveal('.sr10', {delay: 1500, origin: 'top' });