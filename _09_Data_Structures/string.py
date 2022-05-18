string="meena"
print(len(string))


string1="meena"
counter=string1.count('e')
print("count e in meena:"+str(counter))


string2="meena"
print(string2[0:4])


def swap(string):
     start=string[0]
     end=string[-1]
     swapped_string=end+string[1:-1]+start
     print(swapped_string)

swap("meena")


def odd_values_string(str):
    result=" "
    for i in range(len(str)):
        if i % 2 == 0:
            result=result + str[i]
    return result
print(odd_values_string('ace'))


string4="Meena ana gang"
res=len(string4.split())
print("the words count in string"+str(res)) 


string5='Meena AG'
print(string5.lower())


string6='Meena AG'
print(string6.upper())


string7="MeenaA=AG"
print(string7.rsplit('=',1)[0])



string8='meena \n'
print(string8)
print(string8.rstrip())


sentence=input("enter the string:")
longest=max(sentence.split(),key=len)
print("the longest length of string",longest)
print("the length of longest string",len(longest))


