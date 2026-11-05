// ----- Nav bar menu opening -----//

const nav_menu = document.getElementById("nav-menu");
const menu_show_button = document.getElementById("nav-toggle");
const menu_hide_button = document.getElementById("menu_hide_btn");
// Renamed from the legacy "show_menu" to avoid the old unscoped
// .show_menu{left:0!important} rule in style.css, which would have
// fought the new mobile panel's own right/top-anchored positioning.
const show_menu = "nav-open";

if (nav_menu && menu_show_button && menu_hide_button) {
    menu_show_button.addEventListener("click", funShow);
    menu_hide_button.addEventListener("click", funHide);

    // Close the mobile menu after a nav link is selected. Uses the same
    // position-based nav-open class as the open/close buttons above —
    // never toggles display:none, so it can't hide the persistent desktop nav.
    const menuLinks = nav_menu.querySelectorAll("a");
    menuLinks.forEach(function (link) {
        link.addEventListener("click", funHide);
    });

    // Close on an outside tap/click (anywhere that isn't the panel itself
    // or the toggle button that opens it).
    document.addEventListener("click", function (event) {
        if (!nav_menu.classList.contains(show_menu)) return;
        var clickedInsideMenu = nav_menu.contains(event.target);
        var clickedToggle = menu_show_button.contains(event.target);
        if (!clickedInsideMenu && !clickedToggle) {
            funHide();
        }
    });

    // Close on Escape, and return focus to the toggle button so keyboard
    // users land somewhere sensible instead of on a now-hidden link.
    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && nav_menu.classList.contains(show_menu)) {
            funHide();
            menu_show_button.focus();
        }
    });

    // Clear the mobile dropdown's open state the moment the viewport
    // crosses into desktop (768px, the same breakpoint the CSS switches
    // on). Without this, an open mobile menu left open through a resize
    // stays marked open in the DOM/aria-expanded even though desktop
    // shows the links inline instead -- so resizing back down to mobile
    // would have the dropdown pop open again unexpectedly. This fires
    // outside the mobile CSS's own transition breakpoint, so it never
    // animates; it only ever snaps shut instantly.
    var desktopQuery = window.matchMedia && window.matchMedia("(min-width: 768px)");
    if (desktopQuery) {
        var handleDesktopCrossing = function (event) {
            if (event.matches) funHide();
        };
        if (desktopQuery.addEventListener) {
            desktopQuery.addEventListener("change", handleDesktopCrossing);
        } else if (desktopQuery.addListener) {
            desktopQuery.addListener(handleDesktopCrossing);
        }
        if (desktopQuery.matches) funHide();
    }
}

function funShow() {
    if (nav_menu) nav_menu.classList.add(show_menu);
    if (menu_show_button) menu_show_button.setAttribute("aria-expanded", "true");
}

function funHide() {
    if (nav_menu) nav_menu.classList.remove(show_menu);
    if (menu_show_button) menu_show_button.setAttribute("aria-expanded", "false");
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

// Respect the visitor's reduced-motion preference: skip the parallax
// background drift entirely rather than just speeding it up, since it's
// optional decoration and the content is already visible in the DOM by
// default. (Scroll-entrance fades for this page now live in
// scroll-scenes.js / the .scene-content system -- this used to also run a
// separate ScrollReveal-driven fade on the hero, which was removed to
// avoid two independent opacity animations stacking on the same content.)
const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

//---- parallex effect ---//
var scene = document.getElementById('scene');
if (scene && !prefersReducedMotion) {
    var parallex = new Parallax(scene);
}

var heroOrbit = document.getElementById('hero-orbit');
if (heroOrbit && !prefersReducedMotion) {
    var heroOrbitParallax = new Parallax(heroOrbit);
}

//---- desktop header glass darkens slightly once the page has scrolled,
// so nav links stay readable over busy content beneath. Not gated by
// reduced motion -- it's a readability/contrast change (an opacity
// toggle on a background overlay), not decorative motion. ----//
var siteHeader = document.getElementById('site-header');
if (siteHeader) {
    var headerScrollTicking = false;
    var updateHeaderScroll = function () {
        siteHeader.classList.toggle('header-scrolled', window.scrollY > 24);
        headerScrollTicking = false;
    };
    window.addEventListener('scroll', function () {
        if (!headerScrollTicking) {
            window.requestAnimationFrame(updateHeaderScroll);
            headerScrollTicking = true;
        }
    }, { passive: true });
    updateHeaderScroll();
}

//---- cursor/tap-reveal grid: a small patch of fine grid lines follows
// the input over the bar (and the mobile dropdown), fading in/out via
// the .cursor-active class (app.css handles the reveal mask and fade
// transition). Uses Pointer Events so the same code handles a mouse
// (continuous follow while hovering) and a touch tap (brief reveal that
// fades on a timer) on whichever element is actually under the input --
// this is what lets a mouse at phone widths still get the live follow.
// Skipped entirely under reduced motion, matching the plain glass + mesh
// fallback already set up in app.css for that case. ----//
if (!prefersReducedMotion && window.PointerEvent) {
    var setUpGridReveal = function (el) {
        if (!el) return;
        var touchFadeTimer = null;

        var setPosition = function (event) {
            var rect = el.getBoundingClientRect();
            el.style.setProperty('--mx', (event.clientX - rect.left) + 'px');
            el.style.setProperty('--my', (event.clientY - rect.top) + 'px');
        };

        el.addEventListener('pointerdown', function (event) {
            if (event.pointerType !== 'touch') return;
            setPosition(event);
            el.classList.add('cursor-active');
            if (touchFadeTimer) clearTimeout(touchFadeTimer);
            touchFadeTimer = setTimeout(function () {
                el.classList.remove('cursor-active');
            }, 900);
        });

        el.addEventListener('pointermove', function (event) {
            if (event.pointerType !== 'mouse') return;
            setPosition(event);
            el.classList.add('cursor-active');
        });

        el.addEventListener('pointerleave', function (event) {
            if (event.pointerType !== 'mouse') return;
            el.classList.remove('cursor-active');
        });
    };

    setUpGridReveal(siteHeader);
    setUpGridReveal(nav_menu);
}