// TODO
var btns = document.getElementsByClassName("menubutton");
for (var i = 0; i < btns.length; i++) {
	btns[i].addEventListener("click", function() {
	var current = document.getElementsByClassName("active");
	current[0].className = current[0].className.replace("active", "");
	this.className += " active";
	});
}

let options = {
  rootMargin: '-50px 0px -55%'
}

window.addEventListener('DOMContentLoaded', () => {
	const observer = new IntersectionObserver(entries => {
		entries.forEach(entry => {
			const id = entry.target.getAttribute('id');
			if (entry.intersectionRatio > 0) {
				document.querySelector(`nav li a[href="#${id}"]`).classList.add('active');

				//Change the hash in the url
				var hash = window.location.hash;
			    if(hash.length > 0) {
					window.location.hash = id;			    
				}
			} else {
				document.querySelector(`nav li a[href="#${id}"]`).classList.remove('active');
			}
		});
	}, options);

	document.querySelectorAll('section[id]').forEach((section) => {
		observer.observe(section);
	});
	
});