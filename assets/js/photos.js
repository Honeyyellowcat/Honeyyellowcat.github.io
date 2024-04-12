
				// Array of image sources
				var images = ['images/am_me_1.jpg', 
                'images/am_PNAA_1.jpg', 'images/am_PNAA_2.jpg', 
                'images/am_SG_Feature.jpg', 'images/am_me_2.jpg',
                'images/am_me_3.jpg', 'images/am_me_4.jpg', 
				'images/am_me_5.png'
            ]; // Add paths to additional images as needed
			
				// Variable to keep track of the current image index
				var currentImageIndex = 0;
			
				// JavaScript function to handle image change
				function changeProfileImage(step) {
					// Get the profile image element
					var profileImage = document.getElementById('profile-image');
					
					// Increment the image index by the step (1 or -1)
					currentImageIndex += step;
					
					// If the index is out of bounds, loop to the other end
					if (currentImageIndex >= images.length) {
						currentImageIndex = 0;
					} else if (currentImageIndex < 0) {
						currentImageIndex = images.length - 1;
					}
					
					// Set the source of the image to the new image in the array
					profileImage.src = images[currentImageIndex];
				}
			
				// Add event listeners to arrow clicks
				document.querySelector('.arrow-left').addEventListener('click', function() {
					changeProfileImage(-1);
				});
			
				document.querySelector('.arrow-right').addEventListener('click', function() {
					changeProfileImage(1);
				});
			
				// Automatically change image after a certain time
				setInterval(function() {
					changeProfileImage(1);
				}, 5000); // Change every 5 seconds