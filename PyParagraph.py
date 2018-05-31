import os
import string

file_num = 1

file = os.path.join('raw_data','paragraph_'+ str(file_num)+ '.txt')


paragraph_str = ''
with open(file,'r') as txtfile:
    paragraph_str = txtfile.read()



SentenceCount = paragraph_str.count('.')+paragraph_str.count('?') + paragraph_str.count('!') 


letters = string.ascii_letters +" "


for char in paragraph_str:
    if char not in letters:
        paragraph_str = paragraph_str.replace(char, '')



paragraph_list = paragraph_str.split(" ")

letterTotal = 0 
for word in paragraph_list:
    letterTotal += len(word)

word_count = len(paragraph_list)

AvgWordLength = letterTotal/word_count

WordsPerSentence = word_count/SentenceCount

output_file = os.path.join('paragraph_analysis_' + str(file_num)+ '.txt')

with open(output_file,'w') as txtfile:

    txtfile.writelines('Paragraph Analysis\n-----------------\nApproximate Word Count: '
    + str(word_count)+ '\nApproximate Sentence Count: ' + str(SentenceCount) + 
    '\nAverage Letter Count: ' + str(AvgWordLength) + '\nAverage Sentence Length: ' + str(WordsPerSentence))


with open(output_file,'r') as txtout:
    print(txtout.read())