// Array of image sources
var images = [
    'assets/img/SpaceTeam.jpeg',
    'assets/img/am_PNAA_1.jpg',
    'assets/img/am_PNAA_2.jpg',
    'assets/img/SG_Feature.png',
    'assets/img/me_2.jpg',
    'assets/img/me_3.jpg',
    'assets/img/me_4.jpg',
    'assets/img/me_5.jpg'
];

// Variable to keep track of the current image index
var currentImageIndex = 0;
var rotationTimer = null;

function setActiveThumb(index) {
    var thumbs = document.querySelectorAll('.about-gallery-thumb');
    thumbs.forEach(function (thumb, i) {
        thumb.classList.toggle('is-active', i === index);
    });
}

// JavaScript function to handle image change
function changeProfileImage() {
    // Get the profile image element
    var profileImage = document.getElementById('profile-image');
    if (!profileImage) {
        return;
    }

    // Set the source of the image to the next image in the array
    profileImage.src = images[currentImageIndex];
    setActiveThumb(currentImageIndex);

    // Increment the image index
    currentImageIndex++;

    // If the index is out of bounds, loop back to the start
    if (currentImageIndex >= images.length) {
        currentImageIndex = 0;
    }
}

function startRotation() {
    if (rotationTimer) {
        clearInterval(rotationTimer);
    }
    rotationTimer = setInterval(changeProfileImage, 3000);
}

// Build the clickable thumbnail strip from the same images array
function buildThumbnails() {
    var container = document.getElementById('about-gallery-thumbs');
    var profileImage = document.getElementById('profile-image');
    if (!container || !profileImage) {
        return;
    }

    images.forEach(function (src, index) {
        var thumb = document.createElement('button');
        thumb.type = 'button';
        thumb.className = 'about-gallery-thumb';
        thumb.setAttribute('aria-label', 'Show photo ' + (index + 1) + ' of ' + images.length);

        var thumbImg = document.createElement('img');
        thumbImg.src = src;
        thumbImg.alt = '';
        thumb.appendChild(thumbImg);

        thumb.addEventListener('click', function () {
            profileImage.src = src;
            setActiveThumb(index);
            currentImageIndex = index + 1;
            if (currentImageIndex >= images.length) {
                currentImageIndex = 0;
            }
            startRotation();
        });

        container.appendChild(thumb);
    });
}

if (document.getElementById('profile-image')) {
    buildThumbnails();
    // Call the function initially to display the first image
    changeProfileImage();
    // Automatically change image after a certain time
    startRotation();
}
