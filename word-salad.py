import sys
import random

text_in = open(sys.argv[1],'r', encoding = 'utf-8')
text_in = text_in.readlines()

text_in = " ".join(text_in)

text_in = text_in.split()

text_out = ""

for word in text_in:
	if word[-1]=='.' or word[-1]==',':
		if len(word)>4:
			middle= list(word[1:-2])
			random.shuffle(middle)
			middle=''.join(middle)
			word = (word[0]+str(middle)+word[-2:])
	else:
		if len(word)>3:
			middle= list(word[1:-1])
			random.shuffle(middle)
			middle=''.join(middle)
			word = (word[0]+str(middle)+word[-1])
	text_out=text_out+word
	text_out=text_out+' '

print(text_out)

if len(sys.argv)>2:
	file = open(sys.argv[2], 'w+', encoding='utf-8')
	file.write(text_out)
	file.close()