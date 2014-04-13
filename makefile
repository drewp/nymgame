all: index.html game.js word-picker.html word-picker.js word-game.html word-game.js

%.html: %.jade
	/usr/lib/node_modules/nodefront/node_modules/jade/bin/jade < $< > $@
%.js: %.coffee
	coffee -c $<
