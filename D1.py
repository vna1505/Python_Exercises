
cnt=0
wc=[]
sent_list=[]
word_dict={}

sent='hello , how are you , I am you how about you'
sent_list=sent.split()
print(sent_list)


for i in range(len(sent_list)):
    cnt+=1
print('The number of words is: [includes punctuations] ' , cnt)


for i in sent_list:
    wc.append(sent_list.count(i))
print(wc)

print(zip(sent_list,wc))
word_dict=zip(sent_list,wc)
print(set(word_dict))


#hello , how are you , I am you how about you