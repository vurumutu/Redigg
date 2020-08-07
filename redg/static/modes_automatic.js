if (
	localStorage.getItem('color-scheme') === 'dark' ||
	(window.matchMedia('(prefers-color-scheme: dark)').matches &&
		!localStorage.getItem('color-scheme'))
	){
	document.documentElement.setAttribute('color-scheme', 'dark')
}