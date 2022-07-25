# file name: Anagram.py, author: Marina Amorim, version: 1.0, date: 01/29/2020, course: CSCI 262, modification log: completed the anagram function and added more tests to the test function.

#The test function conducts a series of tests by calling testPair.

def test():
  testPair(1,"eat","tea",True)
  testPair(2,'Clint Eastwood','Old West Action',True)
  testPair(3,'arranged','deranged',False)
  testPair(4,'Marina','aniram',True)
  testPair(5,'My name is John','My name is Marina',False)
  testPair(6,'A gentleman','Elegant man',True)
  testPair(7,'Listen','SILENT',True)
  testPair(8,'game','rock',False)

  
  
#The testPair function takes a test number, two words, and the expected result (true if they are anagrams and false otherwise).  It prints a notice of whether or not the anagram function gave the correct answer for these two words.

def testPair(testNumber,word1,word2,expected):
  if anagram(word1,word2)==expected:
    result = "passed"
  else:
    result = "failed"
  print("Test "+str(testNumber)+"  "+result+":"+ word1+" "+word2+" "+str(expected))


#The anagram function takes two words and returns true if they are anagrams and false otherwise.  

def anagram(word1,word2):
# remove the spaces from the words
  word1 = word1.replace(" ", "")
  word2 = word2.replace(" ", "")
# check if both words have the same number of characters
  word1_len = len(word1)
  word2_len = len(word2)

  if word1_len != word2_len:  
    return False
  else:
  #ignore uppercase by turning the words lowercase
    word1 = word1.lower()
    word2 = word2.lower()
    

  #sort the strings to be able to compare
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
  #compare both sorted strings
    for i in range (0,word1_len):
      if word1_sorted[i] != word2_sorted[i]:
        return False
    return True

test()

def stringinputtest():
  testPair(1, 'hello', 5, False) 
  testPair(2, 6, True, False)
  testPair(3, True, 'True', False) 
  testPair(4, 4, "four", False) 
  testPair(5, 123,123,False)
  testPair(6, [0,6],[0,6],False)



stringinputtest()








  