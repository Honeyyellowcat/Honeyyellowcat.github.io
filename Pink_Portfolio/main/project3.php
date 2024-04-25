<!DOCTYPE HTML>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Felicity: Finite Wing</title>
    <!--icon-->
    <link rel='stylesheet' href='https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
    <!--slider-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Swiper/8.2.4/swiper-bundle.css">
    <!--tailwind.css-->
    <script src="https://cdn.tailwindcss.com"></script>
    <!--parallax-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/parallax/3.1.0/parallax.min.js"></script>
    <!--main CSS-->
    <link rel="stylesheet" href="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\css\style.css">
</head>

<body>
    <div class="header text-[#FDFCF3] text-lg font-bold p-6 mx-auto pb-5 pt-5lg:p-14 lg:pt-8 lg:pb-8">
        <nav>
            <ul>
                <li><a href="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\main.html">Home</a></li>
            </ul>
        </nav>
    </div>
		<!-- Wrapper -->
			<div id="wrapper">
				<!-- Main -->
					<section id="main" class="wrapper text-pink">
						<div class="inner">
							<h1 class="text-pink font-bold select-none inline-block uppercase text-3xl md:text-5xl lg:text-6xl py-4">Aerospace Laboratory I: Finite Wing Analysis in the Kirsten Wind Tunnel (KWT)</h1>
							<span class="image fit"><img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_2.jpg" alt="" /></span>
							<p>
								<h2 class="text-3xl">Summary: </h2>
								<ul>
									<p>The experiment investigates propeller geometry and pitch influence on performance metrics. 
										It compares four propellers in a 3x3 wind tunnel and discusses limitations.</p>
								</ul>
							</p>
							<!-- Button to open PDF -->
            				<li class="text-2xl">1. Finite Wings Report: <a href="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\doc\CDR.pdf" target="_blank"><span class="text-[#99ABFF]">Here</span></a></li>
                            <p>
								<h2 class="text-2xl">Abstract:</h2>
								<ul>
									<li>- Explored propeller geometry and pitch influence on performance metrics.</li>
									<li>- Found performance metrics depend on propeller geometry and advance ratio.</li>
									<li>- Highlighted the need for further analysis on propeller design optimization.</li>
								</ul>

								<h2 class="text-2xl">Introduction:</h2>
								<ul>
									<li>- Objective: Measure propeller performance and evaluate pitch influence.</li>
									<li>- Utilized advanced equipment and a 3’x3’ wind tunnel for controlled airflow.</li>
									<li>- Experiment involved testing two propeller models at different pressure values.</li>
								</ul>

								<h2 class="text-2xl">Theory:</h2>
								<ul>
									<li>- Propeller power, efficiency, thrust, and torque equations were explored.</li>
									<li>- Discussed propeller advance ratio and its impact on efficiency and thrust.</li>
									<li>- Formulas for thrust and torque coefficients were provided.</li>
								</ul>

								<h2 class="text-2xl">Methods and Procedure:</h2>
								<ul>
									<li>- Experiment conducted in a 3x3 wind tunnel using various equipment.</li>
									<li>- Data collected included RPM, indicated pressure, drag, torque, and temperature.</li>
									<li>- Propellers tested at different indicated pressures and RPM ranges.</li>
								</ul>

								<h2 class="text-2xl">Results and Discussion:</h2>
								<ul>
									<li>- Thrust trends deviated from expectations, possibly due to data inaccuracies.</li>
									<li>- Efficiency and torque data showed unexpected patterns, requiring further investigation.</li>
									<li>- Limitations of the experiment, including potentiometer and propeller dimensions, were discussed.</li>
								</ul>

								<h2 class="text-2xl">Conclusion:</h2>
								<ul>
									<li>- Results were unexpected, possibly due to limitations in experimental setup.</li>
									<li>- Suggested improvements include digital motor speed control and consistent propeller dimensions.</li>
									<li>- Highlighted the need for future experiments to isolate propeller geometry and pitch effects.</li>
								</ul>
                            </p>
                        </div>
					</section>
			</div>
			<!-- Photo Album Section -->
			<style>
				body {
					margin: 0;
					padding: 0;
				}
	
				#photo-album {
					padding: 20px 0;
					text-align: center;
					height: 100%;
					display: flex;
					flex-direction: column;
					justify-content: center; /* Adjusted to center vertically */
					align-items: center;
				}
	
				.photo-grid {
					display: flex; /* Set the container to use flexbox */
					justify-content: center; /* Center the items horizontally */
					gap: 10px; /* Add gap between items */
					margin-bottom: 20px; /* Add margin at the bottom */
					flex-wrap: wrap; /* Allow items to wrap to the next line */
				}
	
	
				.photo img {
					max-width: 100px; /* Adjust the size of the images */
					height: auto;
					cursor: pointer; /* Change cursor to pointer when hovering over images */
					transition: transform 0.3s ease; /* Add transition for smooth effect */
				}
	
				.photo video {
					max-width: 100px; /* Adjust the size of the video in its default state */
					height: auto;
					cursor: pointer; /* Change cursor to pointer when hovering over the video */
					transition: transform 0.3s ease; /* Add transition for smooth effect */
				}
	
				.photo img.expanded {
					max-width: 30vw; /* Adjust the size of the expanded images */
					position: fixed;
					top: 50%;
					left: 50%;
					transform: translate(-50%, -50%);
					z-index: 9999;
					transition: none; /* Remove the transition effect */
				}
	
				.photo video.expanded {
					max-width: 20vw; /* Adjust the size of the expanded video */
					position: fixed;
					top: 50%;
					left: 50%;
					transform: translate(-50%, -50%);
					z-index: 9999;
					transition: none; /* Remove the transition effect */
				}
			</style>
			</head>
			<body>
	
			<section id="photo-album">
				<h2>Photo Album</h2>
				<div class="photo-grid">
					<div class="photo">
						<img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_1.jpg" alt="Photo 1">
					</div>
					<div class="photo">
						<img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_3.jpg" alt="Photo 2">
					</div>
					<div class="photo">
						<img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_4.jpg" alt="Photo 2">
					</div>
					<div class="photo">
						<img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_5.jpg" alt="Photo 2">
					</div>
					<div class="photo">
						<img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_6.jpg" alt="Photo 2">
					</div>
					<div class="photo">
						<img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_7.jpg" alt="Photo 2">
					</div>
					<div class="photo">
						<img src="C:\Users\every\OneDrive\Desktop\CODE\Pink_Portfolio\main\assets\img\WT_8.jpg" alt="Photo 2">
					</div>
				</div>
			</section>
	
			<script>
				const mediaElements = document.querySelectorAll('.photo img, .photo video');
	
				mediaElements.forEach(media => {
					media.addEventListener('click', () => {
						mediaElements.forEach(m => {
							if (m !== media) {
								m.classList.remove('expanded');
							}
						});
						media.classList.toggle('expanded');
					});
				});
			</script>
			</body>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>