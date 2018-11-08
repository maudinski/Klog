import re
import sys

r = open(sys.argv[1], "r")
w = open("out1.txt", "w")

data = r.read()
data = data.replace("<E>", '\n')
data = data.replace("<T>", '\t')

w.write("%s" % data)

r.close()
w.close()

rr = open("out1.txt", "r")
ww = open("out2.txt", "w")

char_backspace = re.compile(".<B>")
any_backspaces = re.compile("<B>+")

def apply_backspaces(s):
    while 1:
        t = char_backspace.sub("", s)
        if len(s) == len(t):
            # remove any backspaces which may start a line
            return any_backspaces.sub("", t)
        s = t 

for line in rr:
    ww.write ("%s" % apply_backspaces(line) )

rr.close()
ww.close()
    

r = open("out2.txt", "r")
w = open("found.txt", "w")

phone = re.compile(r'(\d{3})[ -]?(\t)?(\d{3}[ -]?(\t)?\d{4})')
email = re.compile(r'.+@.+\..+')
site = re.compile(r'.+\.(co|com|edu|net|org|gov|us)')
card = re.compile(r'\d{4}[ -]?(\t)?\d{4}[ -]?(\t)?\d{4}')
date = re.compile(r'\d{2}[ -/]?(\t)?\d{2}[ -/]?(\t)?\d?\d?\d{2}')
ssn = re.compile(r'\d{3}[ -]?(\t)?\d{2}[ -]?(\t)?\d{4}')

emailFound = False
cardFound = False
phoneFound = False
dateFound = False
ssnFound = False

array = []
l = 0
sitess = 0
for line in r:
    l += 1

    if sitess > 0:
        if (emailFound == True):
            sitess = 0
        if (sitess == 2):
            w.write ( "(Line %d) " % l)
            w.write ("user or email: %s" % line)
        if (sitess == 1):
            w.write ( "(Line %d) " % l)
            w.write ("password: %s" % line)
        sitess -= 1;


    if emailFound == True:
        print( "LINE", l, "PASSWORD:", line)
        w.write ("(Line %d) " % l)
        w.write("password: %s" % line)
    
    emailFound = False
    dateFound = False
    cardFound = False
    phoneFound = False
    ssnFound = False
    
    matchEmail = email.search(line)
    if matchEmail != None:
        emailFound = True
        print( "LINE", l, "EMAIL:", matchEmail.group() )
        w.write ("(Line %d) " % l)
        w.write ("email: %s\n" % matchEmail.group() )
        
    matchSite = site.search(line)
    if matchSite != None and emailFound == False:
        print( "LINE", l, "WEBSITE:", matchSite.group() )
        w.write ("(Line %d) " % l)
        w.write ( "website: %s\n" % matchSite.group() )
        sitess = 2
    
    matchCard = card.search(line)
    if matchCard != None:
        cardFound = True
        print( "LINE", l, "CARD:", matchCard.group() )
        w.write ("(Line %d) " % l)
        w.write ( "card: %s\n" % matchCard.group() )
        
    matchPhone = phone.search(line)
    if matchPhone != None and cardFound == False:
        print( "LINE", l, "PHONE:", matchPhone.group() )
        w.write ("(Line %d) " % l)
        w.write ("phone: %s\n" % matchPhone.group())
        phoneFound = True
    
    matchSSN = ssn.search(line)
    if (matchSSN != None and cardFound == False ):
        print ("LINE", l, "SSN:", matchSSN.group() )
        w.write ("(Line %d) " % l)
        w.write ("ssn: %s\n" %matchSSN.group() )
        ssnFound = True
        
    matchDate = date.search(line)
    if (matchDate != None and cardFound == False and 
        phoneFound == False and ssnFound == False):
        print ( "LINE", l, "DATE:", matchDate.group() )
        w.write ("(Line %d) " % l)
        w.write ("date: %s\n" % matchDate.group() )
        dateFound = True

r.close()
w.close()

r = open("out2.txt", "r")
w = open("raw.txt", "w")

i = 0
for l in r:
    i += 1
    w.write ("%d) " % i)
    w.write ("%s" % l)
r.close()
w.close()
