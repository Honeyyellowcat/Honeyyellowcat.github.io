<script>
    // Get all the images with the class 'photo'
    const photos = document.querySelectorAll('.photo img');

    // Add click event listener to each image
    photos.forEach(photo => {
        photo.addEventListener('click', () => {
            // Toggle the class 'expanded' on click
            photo.classList.toggle('expanded');
        });
    });
</script>
