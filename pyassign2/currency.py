"""Currency.py

__author__ = "Yu Yuanhe"
__pkuid__  = "1700012623"
__email__  = "yuyuanhe@pku.edu.cn"
"""
###  Part of Fuction Def  ###
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

#  Part A  #
def before_space(s):
    """For a string s, get the part before the space.

    Returns: Substring of s; up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    if s[0]!=" " :  
        a1=s.index(" ")
        a=s[:a1]
    return a 

def after_space(s):
    """For a string s, get the part after the space.

    Returns: Substring of s after the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    if s[0]!=" ":
        a1=s.index(" ")
        a=s[a1+1:]
    return a 

#  Part B  #
def first_inside_quotes(s):
    """For a string s,get the first substring of it between two quotes.

    Returns: The first substring of s between two (double) quote characters

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside.
    """
    i1=s.find('"')
    i2=s.find('"',i1+1)
    b=s[i1+1:i2]
    return b

def get_from(json):
    """For the json from the website, get the from value in it.

    Returns: The FROM value in the response to a currency query

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    i=json.find('from')
    i1=i+5
    string=json[i1:]
    b=first_inside_quotes(string)
    return b

def get_to(json):
    """For the json from the website, get the to value in it.

    Returns: The TO value in the response to a currency query

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    i=json.find('to')
    i1=i+3
    string=json[i1:]
    b=first_inside_quotes(string)
    return b

def has_error(json):
    """Judge if there is an error in the json from the website.

    Returns: True if the query has an error; False otherwise

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    if 'true' in json:
        return False
    else:
        return True

#  Part C  #
"""Get the JSON from the website.
"""
def currency_response(currency_from, currency_to, amount_from):
    from urllib.request import urlopen

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

#  Part D  #
def iscurrency(currency):
    jstr=currency_response(currency, 'USD', 2.5)
    if has_error(jstr):
        return False
    else:
        return True
    
def exchange(currency_from,currency_to,amount_from):
    mid=currency_response(currency_from, currency_to, amount_from)
    output=float(before_space(get_to(mid)))
    return output

###  Test Part  ###
def test_before_space():
    assert('I' == before_space('I am anarchy'))
def test_after_space():
    assert('am anarchy' == after_space('I am anarchy')) 
def test_first_inside_quotes():
    assert(first_inside_quotes('"623" 2323"502"')=='623')
def test_get_from():
    assert(get_from('"from":"1.0 United States Dollars","to":"6.680436 Chinese Yuan","success":true,"error":""')=='1.0 United States Dollars')
def test_get_to():    
    assert(get_to('"from":"1.0 United States Dollars","to":"6.680436 Chinese Yuan","success":true,"error":""')=='6.680436 Chinese Yuan')
def test_has_error():    
    assert(has_error('true')==False)
def test_currency_response():    
    assert(currency_response('USD','CNY',1)=='{ "from" : "1 United States Dollar", "to" : "6.680436 Chinese Yuan", "success" : true, "error" : "" }')
def test_iscurrency():    
    assert(iscurrency('233') == False)
def test_exchange():    
    assert(exchange('michelle','anarchy',1)==None)
def test_All():
    test_before_space()
    test_after_space()
    test_first_inside_quotes()
    test_get_from()
    test_get_to()
    test_has_error()
    test_currency_response()
    test_iscurrency()
    test_exchange()
    print("All tests passed")

###  Main Part  ###
def main():
    currency_from=input("The currency you want to exchange from:")
    currency_to=input("The currency you want to exchange to:")
    amount_from=float(input("The number of money you want to exchange:"))

    if exchange(currency_from, currency_to, amount_from)==None:
        print ("Please input the right currencies.")
    else:
        print("The amount of "+currency_to+" is "+str(exchange(currency_from, currency_to, amount_from))+".")

        
if __name__ == '__main__':
    main()


