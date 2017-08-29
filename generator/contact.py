from model.contact import Contact

import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:",["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="data/contacts.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f=a

def random_string(prefix,maxlen):
    symbols=string.ascii_letters+string.digits+" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata=[
    Contact(firstname=random_string("firstname",10), middlename=random_string("middlename",10), lastname=random_string("lastname",10),
            nickname=random_string("nickname",10), title=random_string("title",4), company=random_string("company",10),
            address=random_string("addr",10), home="".join([random.choice(string.digits) for i in range(random.randrange(10))]),
            mobile="".join([random.choice(string.digits) for i in range(random.randrange(10))]),
            work="".join([random.choice(string.digits) for i in range(random.randrange(10))]),
            fax="".join([random.choice(string.digits) for i in range(random.randrange(10))]),
            email=random_string("email",10),email2=random_string("email2",10),email3=random_string("email3",10),
            homepage=random_string("www.",10), byear="".join([random.choice(string.digits) for i in range(4)]),
            ayear="".join([random.choice(string.digits) for i in range(4)]),
            address2=random_string("address2",10), phone2="".join([random.choice(string.digits) for i in range(random.randrange(10))]),
            notes=random_string("notes",10)) for j in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

