=================
Sharevalue
=================

Task
-------
Write a file sharevalue.py such that when we run the command ./sharevalue.py <NASDAQ_symbol_of_company> will give the share value of the company.

Code Description
-----------------
In this code, we import urllib2 package.The urllib2 module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

**share_value Function**

Nasdaq symbol of the company is passed to this function which  inserts it in the url of yahoo sharevalue finder. urllib2.open(url) function is  used to open the url for finding the sharevalue. print_sharevalue() function is then  called from this function.


**print_sharevalue Function**
This function as the name suggests reads the sharevalue file and prints the sharevalue after checking if the NASDAQ symbol is valid. The is    done by checking if the the sharevalue read is equal to 0.0 . If sharevalue is zero , it indicates that the NASDAQ symbol is invalid, hence    prints "invalid nasdaq symbol" . If nasdaq value is valid it prints the corresponding sharevalue.


**link to the code**
`link <https://github.com/elitalobo/HomeTask1>`_


