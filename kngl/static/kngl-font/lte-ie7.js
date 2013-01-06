/* Use this script if you need to support IE 7 and IE 6. */

window.onload = function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'kngl\'">' + entity + '</span>' + html;
	}
	var icons = {
			'icon-new-tab' : '&#xe000;',
			'icon-external-link' : '&#xe001;',
			'icon-github' : '&#xe002;',
			'icon-github-2' : '&#xe003;',
			'icon-github-3' : '&#xe004;',
			'icon-github-4' : '&#xe005;',
			'icon-github-alt' : '&#xe006;',
			'icon-bucket' : '&#xe007;',
			'icon-bitbucket' : '&#xe008;',
			'icon-lp-logo' : '&#xe009;',
			'icon-lp' : '&#xe00a;',
			'icon-linkedin' : '&#xe00b;',
			'icon-linkedin-2' : '&#xe00c;',
			'icon-twitter' : '&#xe00d;',
			'icon-twitter-2' : '&#xe00e;',
			'icon-instagram' : '&#xe00f;',
			'icon-instagram-2' : '&#xe010;',
			'icon-flickr' : '&#xe011;',
			'icon-flickr-2' : '&#xe012;'
		},
		els = document.getElementsByTagName('*'),
		i, attr, html, c, el;
	for (i = 0; i < els.length; i += 1) {
		el = els[i];
		attr = el.getAttribute('data-icon');
		if (attr) {
			addIcon(el, attr);
		}
		c = el.className;
		c = c.match(/icon-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
};