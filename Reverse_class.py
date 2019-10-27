#input: Hello world today
#output : today world Hello

class Word:
    output=[]
    inp=[]

    def __init__(self,sent1):
        inp=sent1.split()
        output= inp[::-1]
        print(output)

if __name__=="__main__":

    sent1 =Word("Hello world today")


