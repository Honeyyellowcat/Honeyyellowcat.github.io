// ----- Nav bar menu opening -----//

const nav_menu = document.getElementById("nav-menu");
const menu_show_button = document.getElementById("nav-toggle");
const menu_hide_button = document.getElementById("menu_hide_btn");
const show_menu = "show_menu";

if (nav_menu && menu_show_button && menu_hide_button) {
    menu_show_button.addEventListener("click", funShow);
    menu_hide_button.addEventListener("click", funHide);

    // Close the mobile menu after a nav link is selected. Uses the same
    // position-based show_menu class as the open/close buttons above —
    // never toggles display:none, so it can't hide the persistent desktop nav.
    const menuLinks = nav_menu.querySelectorAll("a");
    menuLinks.forEach(function (link) {
        link.addEventListener("click", funHide);
    });
}

function funShow() {
    if (nav_menu) nav_menu.classList.add(show_menu);
}

function funHide() {
    if (nav_menu) nav_menu.classList.remove(show_menu);
}

//----- active menu li a -----//
// Only the homepage's own in-page anchor targets (not every element with an id)
const homepageAnchorIDs = ["home", "about", "work", "contact"];
const sections = Array.from(document.querySelectorAll(homepageAnchorIDs.map(id => `#${id}`).join(", ")));

if (sections.length > 0) {
    window.addEventListener("scroll", navHighlighter);
}

function navHighlighter() {
    //Get current scroll position
    let scrollY = window.pageYOffset;

    // now we loop thru sections to get height, top and id valuers for each
    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 50;
        const sectionID = current.getAttribute("id");
        const link = document.querySelector(`.nav_menu a[href*="${sectionID}"]`);
        if (!link) return;

        /*
        -if out current schroll position enters the space where current section on screen is, add
        - To know which link needs an active class, we ise sectionId variable we are getting while
        */
       if(
        (scrollY >= sectionTop) &&
        (scrollY <= sectionTop + sectionHeight)
        ) {
            link.classList.add("active-link");
        } else {
            link.classList.remove("active-link");
        }
    });
};

//----Sliders---//
// Guard against initializing Swiper when no .slide-content element is on
// the page (true on the current homepage) — avoids a console error on load.
var swiper = document.querySelector(".slide-content") ? new Swiper(".slide-content", {
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
}) : null;

//---- parallex effect ---//
var scene = document.getElementById('scene');
if (scene) {
    var parallex = new Parallax(scene);
}

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