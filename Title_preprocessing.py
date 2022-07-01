import json, re, nltk, csv, sys
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.stem.snowball import SnowballStemmer
from preprocessing import Preprocessing

ftag=open('Tags.txt','w',encoding="utf-8")
fclean=open('cleanedTitle.txt','w',encoding="utf-8")
ftrain=open("Train.csv", "rt",encoding="utf-8")

s=set(stopwords.words('english'))
reader = csv.DictReader(ftrain)

i=0
for row in reader:
	try:
		#Data preprocessing
		words=re.sub('[!@%^&*()$:"?<>=~,;`{}|]',' ',str(row['Title']).lower())
		words=Preprocessing(words,s)		
		fclean.write(words+'\n')
		ftag.write(row['Tags']+'\n')
		print("Row Cleaned-",row['Id'])
		i=i+1		
	except Exception as e:
		print("EXCEPTION: ",str(e))
		fclean.write('\n')
		ftag.write('\n')
		i=i-1
		pass
		
fclean.close()
ftag.close()
ftrain.close()

print("Preprocessed the records")


