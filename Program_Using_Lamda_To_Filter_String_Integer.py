User_Input= ["a", 1,3,4, "c", "hello"]
print ("Given list with string and integer is:", User_Input)
String_Filter = filter (lambda a:type(a) == str   ,User_Input)  # Lambda funtion to filter String from the given list
print("The String instances in the given list is :", list (String_Filter))
Interger_Filter = filter (lambda a:type(a) == int   ,User_Input) # Lambda funtion to filter Integer from the given list
print("The Integer instances in the given list is:", list (Interger_Filter))
