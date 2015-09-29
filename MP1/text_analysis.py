'''
This script uses Pattern's sentiment analysis to find the average polarity and subjectivity of collected tweets about presidential candidates
by Ziyu (Selina) Wang
last modified: September 28, 2015
'''
from pattern.en import *	# Importing Patern to be utilized later
# Creating a list with all the candidates names
candidates = ['HillaryClinton','DonaldTrump','BernieSanders','BenCarson','JebBush','TedCruz','MarcoRubio','MikeHuckabee','RandPaul','CarlyFiorina','ScottWalker','JohnKasich',"MartinO'Malley",'ChrisChristie','JimWebb','RickSantorum','BobbyJindal','LincolnChafee','LindseyGraham','GeorgePataki','JimGilmore','JillStein']
# Traverse through the list
for candidate in candidates:
	# Creating three lists for storing data from the sentiment analysis
	analysis = []
	polarity = []
	subjectivity = []
	try:
		with open(candidate+'.txt', 'r') as f1: # Trying to open the .txt file with all the tweets in it
			# Traverse through the file line by line
			for line in f1:
				data = sentiment(line)	# run sentiment analysis on each tweet
				# Storing the analysis data in the corresponding list
				analysis.append(data)
				polarity.append(data[0])
				subjectivity.append(data[1])
	except:
		print 'Running analysis failed'	# Throw an error if the analysis failed to execute
	if analysis:	# if the analysis was succesful
		# Calculating and displaying the number tweets collected
		numberOfTweets = len(analysis)
		print "Number of tweets about " + candidate + ': ' + str(numberOfTweets)
		# Calculating and displaying the average polarity
		averagePolarity = sum(polarity)/len(polarity)
		print candidate + "'s average polarity: " + str(averagePolarity)
		# Calculating and displaying the average subjectivity
		averageSubjectivity = sum(subjectivity)/len(subjectivity)
		print candidate + "'s average subjectivity: " + str(averageSubjectivity)
	else:	# If there are no tweets about a candidate, display this information
		print 'There is no tweets about ' + candidate + ' collected'
	f1.close();	# Close the .txt file to clean up


