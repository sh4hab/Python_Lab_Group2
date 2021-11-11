TestTuple = (1 , 2 , 3)
Testlist = list(TestTuple)
Testlist.append(97101886)
TestTuple = tuple(Testlist)
print(TestTuple)

TestTuple2 = ("shafaei" , "Shokouhi" , "Fattahi" , "Sarzaeem")
TestTuple3 = ("Shrif" , "AmirKabir")

TestTuple_total = (TestTuple , TestTuple2 , TestTuple3)

print(TestTuple_total)
print(TestTuple_total[0][1],"\n",TestTuple_total[2][1])
# The difference is that we can not change tuples , but we can change Lists .
# This means for changing tuples we have to convert it to lists and then use it .