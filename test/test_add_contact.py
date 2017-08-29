# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

#contact = Contact(firstname="Kirill", middlename="A", lastname="Zimin", nickname="kira", title="Mr.", company="Genesys",
#                  address="Sredij pr.88", home="1111", mobile="2222", work="3333", fax="4444", email="a@mail.ru",
#                  email2="b@mail.ru", email3="c@mail.ru", homepage="www.home.ru", byear="2000", ayear="2017",
#                  address2="Moskovsky", phone2="5555", notes="aaa")


def test_test_add_contact(app,json_contact):
    contact=json_contact
    old_contacts=app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts=app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)
