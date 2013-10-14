fcgi_name:=$(shell python random_filename_gen.py)


css:
	compass compile

deploy:
	python htaccess_gen.py $(fcgi_name) > $(fcgi_name).htaccess
	cp app.fcgi $(fcgi_name).fcgi
	rsync $(fcgi_name).htaccess mit:~/web_scripts/.htaccess
	rsync $(fcgi_name).fcgi     mit:~/web_scripts
	
	rsync lti_website.py       mit:~/web_scripts
	rsync bios.csv             mit:~/web_scripts
	rsync deploy-config.py     mit:~/web_scripts/config.py
	rsync config.rb            mit:~/web_scripts
	rsync -r dynamic           mit:~/web_scripts
	rsync -r lib               mit:~/web_scripts
	rsync -r static            mit:~/web_scripts
	
	rm $(fcgi_name).htaccess
	rm $(fcgi_name).fcgi

deploy-real:
	python htaccess_gen.py $(fcgi_name) > $(fcgi_name).htaccess
	cp app.fcgi $(fcgi_name).fcgi
	rsync $(fcgi_name).htaccess mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts/.htaccess
	rsync $(fcgi_name).fcgi     mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts
	
	rsync lti_website.py      mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts
	rsync bios.csv            mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts
	rsync deploy-config.py    mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts/config.py
	rsync config.rb           mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts
	rsync -r dynamic          mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts
	rsync -r lib              mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts
	rsync -r static           mit:/afs/athena.mit.edu/activity/m/mitlti/web_scripts
	
	rm $(fcgi_name).htaccess
	rm $(fcgi_name).fcgi


