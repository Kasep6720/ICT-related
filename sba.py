import os       #import os for library 
import time

#maintext = input("Write something...") # No need anymore cuz we pro and use file instead of typing 

def sub1():
    # Sub-problem 1
    print()
    print("The original text : ")
    print(maintext)
    print()

    # using split() to count words in string
    res = len(maintext.split())
    
    print("Number of words : " + str(res))
    print("Number of characters : ", len(maintext))
    print()
    input()    
        
def sub2():
    # Sub-problem 2
    countA = 0
    print()
    print("The Frequencies of letter: ")
    for i in range(65,91):
        for letter in maintext:
            # count all letters
            if letter == chr(i) or letter == chr(i+32):
                countA = countA+1
        print("Total number of ", chr(i),": ", countA) 
        countA = 0
    print()
    input()
   
def sub3():
    # Sub-problem 3
    # input specific word UI
    os.system('cls')  #clear screen
    print()
    print('**********************************************************')
    print('***********************YLMASS*****************************')
    print('*****************Composition Analyzer*********************')
    print('*************Please input a specific word*****************')
    print('**********************************************************')

    # pls ignore
    Nigger = input("Specific Word: ")
    print()
    LilNigger = Nigger.lower()
        
    def count(elements):
        elements1 = elements.lower()
        # check if each word has '.' at its last. If so then ignore '.'
        if elements1[-1] == '.':
            elements1 = elements1[0:len(elements1) - 1]
            
        if elements1 in allwordsintext:
            allwordsintext[elements1] += 1
     
        # if the allwordsintext does not have the key as "elements" then create a key "elements" and assign its value to 1.
        else:
            allwordsintext.update({elements1: 1})
    
    allwordsintext = {}
    
    # split all the word of the string.
    lst = maintext.split()
    
    # take each word from lst and pass it to the method count.
    for elements in lst:
        count(elements)
     
    # print the keys and its corresponding values.
    for allKeys in allwordsintext:
        
        # just in case might need it somewhere
        SmolallKeys = allKeys[0].lower() + allKeys[1:]
    
        if allKeys == LilNigger:
            
            print ("Frequency of", allKeys, end = " ")
            print (":", end = " ")
            print (allwordsintext[allKeys], end = " ")
            print()
    input()

def sub4():
    # Sub-problem 4
    print()
    print("The original text : ")
    print(maintext)
    print()
    OrgSentence = maintext.count('.')+maintext.count('!')+maintext.count('?')+maintext.count('...')
    Gays = maintext.count('Dr.')+maintext.count('Esq.')+maintext.count('Hon.')+maintext.count('Jr.')+maintext.count('Mr.')+maintext.count('Mrs.')+maintext.count('Ms.')+maintext.count('Messrs.')+maintext.count('Mmes.')+maintext.count('Msgr.')+maintext.count('Prof.')+maintext.count('Rev.')+maintext.count('Rt. Hon.')+maintext.count('Sr.')+maintext.count('St.')
    print('Total number of sentences:',int(OrgSentence - Gays))
    c = maintext.split('\n\n')
    print('Total number of paragraphs:',len(c))
    input()

def sub5():
    # Sub-problem 5
    os.system('cls')  #clear screen
    stupidassmffunctionwords=['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'be', 'became', 'because', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both', 'but', 'by', 'can', 'cannot', 'could', 'dare', 'despite', 'did', 'do', 'does', 'done', 'down', 'during', 'each', 'eg', 'either', 'else', 'elsewhere', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'first', 'for', 'former', 'formerly', 'from', 'further', 'furthermore', 'had', 'has', 'have', 'he', 'hence', 'her', 'here', 'hereabouts', 'hereafter', 'hereby', 'herein', 'hereinafter', 'heretofore', 'hereunder', 'hereupon', 'herewith', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'i', 'ie', 'if', 'in', 'indeed', 'inside', 'instead', 'into', 'is', 'it', 'its', 'itself', 'last', 'latter', 'latterly', 'least', 'less', 'lot', 'lots', 'many', 'may', 'me', 'meanwhile', 'might', 'mine', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'namely', 'near', 'need', 'neither', 'never', 'nevertheless', 'next', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'oftentimes', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'per', 'perhaps', 'rather', 're', 'same', 'second', 'several', 'shall', 'she', 'should', 'since', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'still', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereabouts', 'thereafter', 'thereby', 'therefore', 'therein', 'thereof', 'thereon', 'thereupon', 'these', 'they', 'third', 'this', 'those', 'though', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'under', 'until', 'up', 'upon', 'us', 'used', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'whyever', 'will', 'with', 'within', 'without', 'would', 'yes', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves']
    d = maintext.split()
    print('Total number of function words:')
    for j in range(len(stupidassmffunctionwords)):
        if d.count(stupidassmffunctionwords[j]) >= 1:
            print(stupidassmffunctionwords[j],d.count(stupidassmffunctionwords[j]))
    input()

def bonus():
    #Bonus  
    print("")
    print("Made by Kasep6720")
    print("")
    print("Reference:")
    print("UI from Shiu Shiu")
    print("Some codes from bd")
    print("https://www.geeksforgeeks.org/find-frequency-of-each-word-in-a-string-in-python/")
    print("https://www.geeksforgeeks.org/python-program-to-calculate-the-number-of-words-and-characters-in-the-string/")
    print("https://www.w3schools.com/python/python_try_except.asp")
    print("https://www.btb.termiumplus.gc.ca/tpv2guides/guides/wrtps/index-eng.html?lang=eng&lettr=indx_catlog_a&page=9NBnYuQ324Yc.html")
    print("")
    print("Thank you!")
    input()

datext = "text.txt"

if __name__ == "__main__" :
    choice = ''
    while (choice!='H' and choice!='h'):
        os.system('cls')  #clear screen
        try:
            f = open(datext, "r")
            maintext = f.read()
        except:
            print("Error")
            print("File not found, or language not supported")
            print("Please enter another .txt file")
            time.sleep(2.2)
            print('**********************************************************')
            print('***********************YLMASS*****************************')
            print('*****************Composition Analyzer*********************')
            print('******************Changing text file**********************')
            print('**********************************************************')
            print("Current text:", datext)
            datext = input("Text File Name: ")
            os.system('cls')  #clear screen
        else:
            f = open(datext, "r")
            maintext = f.read()
            print('**********************************************************')
            print('***********************YLMASS*****************************')
            print('**************Composition Analyzer************************')
            print('************A.Total Number of words and characters *******')
            print('************B.Frequencies of letter **********************')
            print('************C.Frequencies of a given word ****************')
            print('************D.Total Number of sentences and paragraphs****')
            print('************E.Total Number of function word **************')
            print('************F.Change File ********************************')
            print('************G.Credits ************************************')
            print('************H.Exit ***************************************')
            print('**********************************************************')
            choice = input("Input a choice (A,B,C,D,E,F,G,H,):    ")
            while ((choice<'A') or (choice>'H')) and ((choice<'a') or (choice>'h')):
                print("Input out of range, please input again.") 
                choice = input("Input a choice (A,B,C,D,E,F,G,H):    ")
            if (choice == 'A' or choice == 'a'):
                sub1()
            if (choice == 'B' or choice == 'b'):
                sub2()
            if (choice == 'C' or choice == 'c'):
                sub3()
            if (choice == 'D' or choice == 'd'):
                sub4()
            if (choice == 'E' or choice == 'e'):
                sub5()
            if (choice == 'F' or choice == 'f'):
                os.system('cls')  #clear screen
                print('**********************************************************')
                print('***********************YLMASS*****************************')
                print('*****************Composition Analyzer*********************')
                print('******************Changing text file**********************')
                print('**********************************************************')
                print("Current text:", datext)
                datext = input("Text File Name: ")
            if (choice == 'G' or choice == 'g'):
                bonus()
    print('*************************Bye Bye!****************************')
    
