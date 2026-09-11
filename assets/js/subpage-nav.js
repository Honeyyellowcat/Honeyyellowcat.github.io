// Single shared mobile-menu implementation for subpage headers.
// Intentionally does not use a "hidden" (display:none) class toggle on
// anything that is also relied on at desktop widths — .subpage-nav is
// only ever hidden by default inside a max-width media query in
// assets/css/style.css, so this script can never hide the desktop nav.
document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('subpageMenuBtn');
    var nav = document.getElementById('subpageNav');
    if (!btn || !nav) return;

    function closeMenu() {
        nav.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
    }

    function openMenu() {
        nav.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
    }

    btn.addEventListener('click', function () {
        if (nav.classList.contains('is-open')) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    nav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && nav.classList.contains('is-open')) {
            closeMenu();
            btn.focus();
        }
    });
});
