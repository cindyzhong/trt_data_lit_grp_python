FAQs We Got From Lesson 1

Below are some commonly asked questions and answers to them:

1. Compatibility with Python 3.5
If you are running Python 3.5, please refer to README - Python 3 Users.MD

2. Why am I not able to pip install?
If you are using Mac, and you are getting unauthorized access try
```
sudo pip install xxxx
```

If you are using Windows, and you are getting pip install unauthorized access error try to "Run as an Adminstrator"

3. what is key/access/customer secret? What are they used for?
Consumer: A website or application that uses OAuth to access the Service Provider on behalf of the User.

Consumer Key: A value used by the Consumer to identify itself to the Service Provider. (see as account name) 

Consumer Secret: A secret used by the Consumer to establish ownership of the Consumer Key. (see as password) 

Access Token: A value used by the Consumer to gain access to the Protected Resources (like user’s post) on behalf of the User, instead of using the User's Service Provider credentials. 

Token Secret: A secret used by the Consumer to establish ownership of a given Token. 

4. I have pip installed a package but still not able to import it
Check where your default python package directory is, you might have multiple versions of python installed on your computer
More Information: http://stackoverflow.com/questions/32680081/importerror-after-successful-pip-installation

5. I pasted the code but not able to run it?
Make sure the extension of your file is .py



