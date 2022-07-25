# file name: RussianPendant.py, author: Marina Amorim, version: 1.0, date: 04/05/2021, course: CSCI 262, implemented the russian peasant multiplication algorithm.

def russianMultiply(n,m):
    # initialize the multiplication result to zero
    multResult= 0
    # initialize the multiplication result to zero
    countAddends = 0
    print("---------------")
    print("n    m")
    print("---------------")
    print(n," ",m)

    # Until the second number is not one
    while (n >= 1):
        # if the n is even divide n by 2 and double m
        if (n % 2 == 0):
            n = int(n/2)
            m = 2*m
            print(n," ",m)
        # else divide n-1 by 2 and double m
        else:
            n = int((n-1)/2)
            multResult= multResult + m
            countAddends+=1
            m = m*2
            if(n!=0):
                print(n," ",m," ",multResult)
    print("           ----")
    print("          ",multResult)
    print("---------------")
    print([int(multResult + n), countAddends])
        
    # return the array with the result and the count of addends
    return [int(multResult + n), countAddends]
    
 

def testCasesA(testNumber,n,m,expectedResult):
  actualResult = russianMultiply(n,m)
  if actualResult == expectedResult: print ("Test",testNumber,"passed.")
  else: print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)


def test():
  testCasesA(1,50,65,[3250,3])
  testCasesA(2,9,27,[243,2])
  testCasesA(3,15,10,[150,4])
  testCasesA(4,16,35,[560,1])

  


test()

""" Expected tables for the tests:
Test 1:
n    m
50   65
25   130
12   260   130
6   520
3   1040
1   2080   1170
           3250

Test 2:
n    m
9   27
4   54   27
2   108
1   216
           243

Test 3:
n    m
15   10
7   20   10
3   40   30
1   80   70
            150
Test 4:
n    m
16   35
8   70
4   140
2   280
1   560
           560 """



