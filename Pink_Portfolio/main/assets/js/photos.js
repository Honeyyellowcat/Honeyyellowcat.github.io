// Array of image sources
var images = [
    'assets/img/me_1.jpg', 
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

// JavaScript function to handle image change
function changeProfileImage() {
    // Get the profile image element
    var profileImage = document.getElementById('profile-image');

    // Set the source of the image to the next image in the array
    profileImage.src = images[currentImageIndex];

    // Increment the image index
    currentImageIndex++;

    // If the index is out of bounds, loop back to the start
    if (currentImageIndex >= images.length) {
        currentImageIndex = 0;
    }
}

// Call the function initially to display the first image
changeProfileImage();

// Automatically change image after a certain time
setInterval(changeProfileImage, 3000); // Change every 3 seconds
