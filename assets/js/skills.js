function toggleSection(id) {
    const section = document.getElementById(id);
    const icon = document.getElementById(`icon-${id}`);
    if (section.classList.contains('hidden')) {
        section.classList.remove('hidden');
        icon.classList.add('rotate');
    } else {
        section.classList.add('hidden');
        icon.classList.remove('rotate');
    }
}
function changeImage(newSrc) {
    const img = document.getElementById('profile-image');
    img.src = newSrc;
}
