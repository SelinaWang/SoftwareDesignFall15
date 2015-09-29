'''
This script uses Pattern and Twitter API to collect tweets about presidential candidates in the past 30 seconds
by Ziyu (Selina) Wang
last modified: September 28, 2015
'''
from pattern.web import *	# Importing Patern to be utilized later
# Creating a list with all the candidates names
#candidates = ['HillaryClinton','DonaldTrump','BernieSanders','BenCarson','JebBush','TedCruz','MarcoRubio','RandPaul','CarlyFiorina','JohnKasich',"MartinO'Malley",'ChrisChristie','JimWebb','JillStein','RickSantorum','BobbyJindal','LincolnChafee','LindseyGraham','GeorgePataki','JimGilmore','MikeHuckabee','ScottWalker']
candidates = ['GeorgePataki','JimWebb',"MartinO'Malley",'ChrisChristie','JimGilmore','LindseyGraham','LincolnChafee','BobbyJindal','RickSantorum','JillStein']
# Creating a list with all the candidates names in reversed order (in case we need to traverse the original list backwards to collect data for all the candidates)
reversedCandidates = list(reversed(candidates))
# Traverse through the list
for candidate in candidates:
# for candidate in reversedCandidates:	# swap with the last line when traversing the original list backwards
	fileName = candidate+'.txt'	# Name the text file under the candidate's name coerced with +.txt
	try:
		file = open(fileName,'a')   # Trying to create a new file or open an existing one
	except:
		print('Cannot create/open the file')	# If failed to create/open one, through an exception
	s = Twitter().stream(candidate)	# using Pattern and Twitter API to collect tweets about the candidate
	print candidate
	# Storing the tweets in the past 30 seconds into the plain text file
	for i in range(30):	# If there are tweets in the stream
		time.sleep(1)
		s.update(bytes=1024)
		if s:	
			try:
				file.write(s[-1].text+'\n')
				print s[-1].text
			except:
				pass	# The tweet did not have text in it so skip to the next one
	file.close()	# Close the .txt file to clean up

