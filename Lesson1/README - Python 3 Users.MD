#Modifications to Cindy's code for those using Python 3.x instead of 2.7.

###print
In Python 3, you need parentheses in print statement, or you get syntax error. So lines 30 & 31 need to be changed to:
```
print (user_timeline[0]['text'])
print (user_timeline[0]['user']['followers_count'])
```

###L aka long integer
All integers in Python 3 are long, so there is no need to designate in the value. So line 32 needs to be changed to:
```
max_id = -1 #If results only below a specific ID are, set max_id to that ID
```

###Basemap
Basemap is not officially supported in Python 3 yet. You will probably get an error if you try to `conda install` or `pip install`. Follow the answer in this Stack Overflow thread to install.
* http://stackoverflow.com/questions/35716830/basemap-with-python-3-5-anaconda-on-windows
