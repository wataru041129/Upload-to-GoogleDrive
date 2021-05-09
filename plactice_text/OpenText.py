f = open('sample.txt','w',encoding='UTF-8')

f.write('こんにちは\n')

detalist = ['お元気ですか？\n','それではまた\n']
f.writelines(detalist)

f.close()