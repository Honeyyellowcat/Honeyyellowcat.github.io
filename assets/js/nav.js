document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('nav-toggle');
    const menu = document.getElementById('nav-menu');
    
    menuToggle.addEventListener('click', function () {
        menu.classList.toggle('hidden'); // Add or remove the 'hidden' class
    });

    const menuLinks = document.querySelectorAll('#nav-menu a');
    menuLinks.forEach(function (link) {
        link.addEventListener('click', function () {
            menu.classList.add('hidden'); // Hide the menu when a link is clicked
        });
    });

    const menuHideBtn = document.getElementById('menu_hide_btn');
    menuHideBtn.addEventListener('click', function () {
        menu.classList.add('hidden'); // Hide the menu when the close button is clicked
    });
});
