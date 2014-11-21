from BeautifulSoup import BeautifulSoup
#from pyttsk import pyttsk

'''
imports BeautifulSoup package used for parsing
through the webpage and retrieving required contents.
'''
import urllib2
'''
imports urllib2 required to open the webpage corresponding
through the url passed to it.
'''
# big_list = collections.defaultdict(str)
tree = {}
import sys


def Planet_parser():
    print "                MINI BENGALI COOKBOOK              "+"\n"
    # engine = pyttsx.init()
    # engine.say("Mini Benagli CookBook")
    # engine.runAndWait()
    print "Loading list of Bengali dishes..."
    x = 16
    e = 1
    while e < 16:
        url = "http://allrecipes.co.in/recipes/tag-324/bengali-recipes.aspx"
        if e > 1:
            url = url + "?page=" + str(e)
        contents = urllib2.urlopen(url).read()
        soup = BeautifulSoup(contents)
        soup.prettify()
        Author = soup.findAll('div', {'class': 'col-sm-7'})
        count1 = len(Author)  # counts the no of div tags in Author

        i = 0
        while i < count1:
            link = Author[i].find('a').get('href')
            title = Author[i].find('a').text  # prints author of the blog
            tree[title] = link
            i = i + 1
        e = e + 1
        for key, value in tree.iteritems():
            print key+"\n"
    dish = raw_input("Enter the name of the dish you would like to cook: ")
    f = 0
    while f == 0:
        for key, value in tree.iteritems():
            if dish in key:
                f = 1
                dishname = key
                dishlink = value
                break
        if f == 0:
            print "Dish not found! Please enter the name of the dish again."
            dish = raw_input('''Enter the name of the dish you would like to
                             cook: ''')
    print dishname.upper()
    print "\n" + "INGREDIENTS:" + "\n"
    url = dishlink
    contents = urllib2.urlopen(url).read()
    soup = BeautifulSoup(contents)
    soup.prettify()
    ingr = soup.find('section', {'class': 'recipeIngredients'})
    ingred = ingr.find('ul')
    # print ingred
    ingredients = ingred.findAll('li')
    count1 = len(ingredients)  # counts the no of div tags in Author
    i = 0
    while i < count1:
        ingre = ingredients[i].find('span').text  # pr
        print ingre
        i = i + 1
    print "\n" + "INSTRUCTIONS:"
    inst = soup.find('section', {'class': 'recipeDirections'})
    instr = soup.find('ol')
    instructions = instr.findAll('li')
    count1 = len(instructions)  # counts the no of div tags in Author
    i = 0
    while i < count1:
        instru = instructions[i].find('span').text  # pr
        print instru
        i = i + 1
    print "\n HAPPY COOKING!\n"

if __name__ == '__main__':
    Planet_parser()
    sys.exit(1)  # exits
