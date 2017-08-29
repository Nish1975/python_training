# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

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
            notes=random_string("notes",10)) for j in range(2)
]

#contact = Contact(firstname="Kirill", middlename="A", lastname="Zimin", nickname="kira", title="Mr.", company="Genesys",
#                  address="Sredij pr.88", home="1111", mobile="2222", work="3333", fax="4444", email="a@mail.ru",
#                  email2="b@mail.ru", email3="c@mail.ru", homepage="www.home.ru", byear="2000", ayear="2017",
#                  address2="Moskovsky", phone2="5555", notes="aaa")


@pytest.mark.parametrize("contact",testdata,ids=[repr(x) for x in testdata])
def test_test_add_contact(app,contact):
    old_contacts=app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts=app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)
