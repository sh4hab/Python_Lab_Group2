TestList = [1 , 2 , 3 , 4]
print(TestList)
TestList.append(97101886)
print(TestList)


# section 2

TestList2 = ['amin' , 'amirhosein' , 'mohsen']
TestList3 = ['Sharif' , "AmirKabir"]

TestList_total = TestList + TestList2 + TestList3
print(TestList_total)
TestList_total = [TestList , TestList2 , TestList3]
print(TestList_total)
print(TestList_total[1][1])