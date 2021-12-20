# MY SAT TOOLS KIT
#### license : MIT license   
#### author：0764lbc

## Quick Start
1. make sure that you have installed Python and one kind of Python IDE 
2. open main.py and run 
PS : how to interact with Python? ----> [bilibili](https://search.bilibili.com/all?keyword=python%20%E7%8E%AF%E5%A2%83&from_source=webtop_search&spm_id_from=333.851)

## version --0.01
1.add main.py func.py object.py   
2.capable for read a clause and store it as a class  
3.And it could resolve unitary clause for maximal time   
2021-11-25

## version --0.0.2
1.Fixed bugs of return type in function -> count_var_in_clause_with_bool_and_int  
2.Add function plain_text   
3.Adds some data segment to the object clause 
2021-11-26

## version --0.0.3
1.Generate the data structure of params   
2.Add some functions for tautology and make some improvement   
2021-11-27

## version --0.0.4
1.Add solution in obj clause and some func  
2.Improve output() -> show()  
3.But if I use the split func, I can't recursively deliver the keys to the first sentence, so how do you organize your data? think about it!!!!  
4.The next step is to implement the processing function and the final display function.
I want to finish this damn sat  
2021-11-28

## version --0.0.5
1.Add process func to find keys  
2.Add time module to cal time usage   
3.Could find keys in simple clauses  
4.The dawn of victory is at hand!  
2021-11-29

## release version -- 1.0.0
1.Rewrite obj and func  
2.Changes the data structure stored clauses -> set (which is faster to query)  
3.Using copy.deepcopy to avoid memory leak

#### improvement direction:  
1. using func plain_text() in process()
2. using cpp to be faster
3. using cProfile to analysis performance
#### dependency
1. python version >= 3.8  

2021-12-6
