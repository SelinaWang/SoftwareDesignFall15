from pattern.web import *
candidates = ['HillaryClinton','DonaldTrump','BernieSanders','BenCarson','JebBush','TedCruz','MarcoRubio','MikeHuckabee','RandPaul','CarlyFiorina','ScottWalker','JohnKasich',"MartinO'Malley",'ChrisChristie','JimWebb','RickSantorum','BobbyJindal','LincolnChafee','LindseyGraham','GeorgePataki','JimGilmore','JillStein']
reversedCandidates = list(reversed(candidates))
#for candidate in candidates:
for candidate in reversedCandidates:
	fileName = candidate+'.txt'  # Name of text file coerced with +.txt
	try:
		file = open(fileName,'a')   # Trying to create a new file or open one
	except:
		print('Something went wrong! Can\'t tell what?')
	s = Twitter().stream(candidate)
	print candidate
	for i in range(30):
		time.sleep(1)
		s.update(bytes=1024)
		file.write(s[-1].text+'\n') if s else ''
		print s[-1].text if s else ''
	file.close()

