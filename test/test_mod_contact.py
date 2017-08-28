from model.contact import Contact
from random import randrange

def test_mod_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(
            Contact(firstname="Kirill", middlename="A", lastname="Zimin", nickname="kira", title="Mr.",
                    company="Genesys",
                    address="Sredij pr.88", home="1111", mobile="2222", work="3333", fax="4444", email="a@mail.ru",
                    email2="b@mail.ru", email3="c@mail.ru", homepage="www.home.ru", byear="2000", ayear="2017",
                    address2="Moskovsky", phone2="5555", notes="aaa"))

    contact=Contact(firstname="KirillA", middlename="AA", lastname="ZiminA", nickname="kiraA", title="Mr.A", company="GenesysA",
                                address="Sredij pr.88A", home="11119", mobile="22229", work="33339", fax="44449", email="a@mail.ru9",
                                email2="b@mail.ru9", email3="c@mail.ru9", homepage="www.home.ru9", byear="2001", ayear= "2018", address2="Moskovsky1", phone2="55559", notes="aaa9")

    old_contacts=app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id=old_contacts[index].id
    app.contact.mod_contact_by_index(index,contact)
    new_contacts=app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index]=contact
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)

