compass:
	compass compile

deploy:
	rsync app.fcgi mit:~/web_scripts
	rsync lti_website.py mit:~/web_scripts
	rsync bios.csv mit:~/web_scripts
	rsync config.py mit:~/web_scripts
	rsync config.rb mit:~/web_scripts
	rsync config.rb mit:~/web_scripts
	rsync -r dynamic mit:~/web_scripts
	rsync install.sh mit:~/web_scripts
	rsync -r lib mit:~/web_scripts
	rsync -r static mit:~/web_scripts
	rsync .htaccess mit:~/web_scripts
