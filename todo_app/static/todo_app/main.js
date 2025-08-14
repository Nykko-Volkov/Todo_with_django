// Animated UI for Todo App
document.addEventListener('DOMContentLoaded', function() {
	// Animate todos on load
	document.querySelectorAll('ul li').forEach((li, i) => {
		li.style.opacity = 0;
		li.style.transform = 'translateY(30px)';
		setTimeout(() => {
			li.style.transition = 'opacity 0.6s cubic-bezier(.4,2,.6,1), transform 0.6s cubic-bezier(.4,2,.6,1)';
			li.style.opacity = 1;
			li.style.transform = 'none';
		}, 100 + i * 120);
	});

	// Input focus effect
	document.querySelectorAll('input[type="text"], input[type="password"]').forEach(input => {
		input.addEventListener('focus', function() {
			input.style.boxShadow = '0 0 0 2px #2193b0';
		});
		input.addEventListener('blur', function() {
			input.style.boxShadow = '';
		});
	});
});

