""" 1. Write a script, data_types.py, to:
○ Create variables of each primitive data type (int, float, str, bool).
○ Perform a few operations: arithmetic (on int and float), string concatenation, and
logical operations.
○ Create a dictionary to store and display these variables by their types as keys
(e.g., int: [10, 20]).
 """

#Creating Primitive datatypes
data_int:int=20
data_float:float=10.3
data_str:str='raman'
data_bool:bool=True

#Operations on each primitive data type
print(data_int+1) #arithmetic operations on int
print(data_float+0.3) #arithemetic operations on float
print(data_str+' Neupane') #string concatenation
print(data_bool and False) #logical operations

#Creating dictionary to store and display these variables by their types as keys
data_dict={'int':data_int,'float':data_float,'str':data_str,'bool':data_bool}
print(data_dict)
