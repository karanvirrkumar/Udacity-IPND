ques=['Full form of HTML is _1_.This language is used to make _2_ pages._3_ tag is used for largest heading._4_ tag is used to highlight the text.',
      'Full form of CSS is _1_.Types of CSS are _2_ , _3_ and_4_ ',
      'Programming language used in this game is _1_.It is used for _2_ development.This uses _3_ for compilation.This language supports _4_ oriented programming']
answer=[['hyper text markup language','web','h1','mark'],
        ['cascading style sheet','external','internal','inline'],
        ['python','web','interpreter','object']]
levels=['1','2','3']
no_of_blanks=4
def main():
    print ("1.Easy"+" "*5+"2.Difficult"+" "*5+"3.Expert")
    index=input("Enter level number  you want to play..")
    print (index)
    if(index in levels):
        index=int(index)
        index=index-1
        print (ques[index])
        ans(index)
    else:
        print ("You have entered wrong level number.Please try again.. ")
        main()
def ans(ques_index):
    ans_index=0
    while(ans_index<no_of_blanks):
        var=input("Enter "+str(ans_index+1)+" blank...").lower()
        string=ques[ques_index]
        toreplace=("_"+str(ans_index+1)+"_")
        string=string.replace(toreplace,var)
        if(var==answer[ques_index][ans_index]):
            ques[ques_index]=string
            print( "\n"+"You entered correct answer :)"+"\n")
            print (string)
            ans_index=ans_index+1
        else:
            print ("you entered wrong answer try again!!")

print ("Welcome to Ques Game...")
play='y'
while(play=='y'):
    main()  
    print( "\n"+"Congratulations you have completed current level :)"+"\n")
    play=input("To continue playing press 'y' else press 'n'.. :)").lower()
print ("Thank you for playing the game :)")
