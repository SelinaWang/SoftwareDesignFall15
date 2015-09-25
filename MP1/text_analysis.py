from pattern.en import *
candidates = ['HillaryClinton','DonaldTrump','BernieSanders','BenCarson','JebBush','TedCruz','MarcoRubio','MikeHuckabee','RandPaul','CarlyFiorina','ScottWalker','JohnKasich',"MartinO'Malley",'ChrisChristie','JimWebb','RickSantorum','BobbyJindal','LincolnChafee','LindseyGraham','GeorgePataki','JimGilmore','JillStein']
for candidate in candidates:
	analysisName = candidate+'_analysis.txt'  # Name of text file coerced with +.txt
	polarityName = candidate+'_polarity.txt'
	subjectivityName = candidate+'_subjectivity.txt'
	try:
		with open(candidate+'_analysis.txt', 'a') as f1, open (candidate+'_polarity.txt','a') as f2, open (candidate+'_subjectivity.txt','a') as f3: # Trying to create a new file or open one
			pass
	except:
		print('Something went wrong! Can\'t tell what?')
	f1.close()
	f2.close()
	f3.close()

for candidate in candidates:
	analysis = []
	polarity = []
	subjectivity = []
	try:
		with open(candidate+'.txt', 'r') as f1, open (candidate+'_analysis.txt','w') as f2, open (candidate+'_polarity.txt','w') as f3, open (candidate+'_subjectivity.txt','w') as f4:
			for line in f1:
				data = sentiment(line)
				datastr = str(sentiment(line))
				analysis.append(data)
				f2.write(datastr+'\n')
				datastr.split()
				polarity.append(data[0])
				f3.write(datastr[0]+'\n')
				subjectivity.append(data[1])
				f4.write(datastr[1]+'\n')
	except IOError as e:
		print 'Operation failed: %s' % e.strerror
	f1.close();
	f2.close();
	f3.close();
	f4.close();
	averagePolarity = sum(polarity)/len(polarity)
	print candidate + ' average polarity: ' + str(averagePolarity)
	averageSubjectivity = sum(subjectivity)/len(subjectivity)
	print candidate + ' average subjectivity: ' + str(averageSubjectivity)
	# for data in analysis:
	# 	print data.split()
		#print data[3]


# for candidate in candidates:
# 	file = open(candidate+'_analysis.txt', 'r')
# 	for line in file:
# 		int(line)