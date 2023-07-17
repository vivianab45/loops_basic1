# #Basic - Print all integers from 0 to 150.
# for i in range (151):
#     print (i)

# # Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# for i in range (5,1005,5):
#     print(i)

# Print integers 1 to 100. 
# If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def counting_dojo ():
    for i in range(1,101):
        if i%5 ==0:
            print ("Coding")
        elif i%10==0:
            print ("Coding Dojo")
        else: print (i)

counting_dojo()

# # Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

odd_sum=0
for i in range(0,500001):
    if i%2==1:
        odd_sum= odd_sum+i
print (f"The final sum is {odd_sum}")

# # Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

# for i in range(2018,0,-4):
#     print(i)

# # Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

# low_num=2
# high_num=9
# mult=3

# for i in range(low_num,high_num+1):
#     if i % mult==0:
#         print (i)




