
text = 'Mama myla ramu.'
file_text = open('text.txt','w')
file_text.write(text)
file_text.seek(0)

file_text = open('text.txt','r')
text = file_text.read().lower()
result = dict()

file_analysis = open('analysis.txt','w')
long = 0
for letter in text:
   if ord('a') <= ord(letter) <= ord('z'):
       position = result.get(letter, 0)
       result[letter] = position + 1
       long += 1
lout = [(k, "{:5.3f}".format(result[k]/long)) for k in result.keys()]
lout.sort(key = lambda x: x[0])
lout.sort(key = lambda x: x[1], reverse = True)
result_sorted = "\n".join([i[0] + " " + i[1] for i in lout])
file_analysis.write(result_sorted)

file_text.close()
file_analysis.close()












# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# clear_text =''.join(symbol for symbol in text if symbol.isalnum())
# for element in set(text):
#     if element in alphabet:
#         result[element] = round(text.count(element) / len(clear_text), 3)
# for caple in sorted(result.items(), reverse =True, key=lambda para: (para[1], para[0])):
#     file_analysis.write(str(caple))
