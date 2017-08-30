from model.contact import Contact
import random


def test_mod_contact_name(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create_contact(
            Contact(firstname="Kirill", middlename="A", lastname="Zimin", nickname="kira", title="Mr.",
                    company="Genesys",
                    address="Sredij pr.88", home="1111", mobile="2222", work="3333", fax="4444", email="a@mail.ru",
                    email2="b@mail.ru", email3="c@mail.ru", homepage="www.home.ru", byear="2000", ayear="2017",
                    address2="Moskovsky", phone2="5555", notes="aaa"))

    contact1 = Contact(firstname="KirillA", middlename="AA", lastname="ZiminA", nickname="kiraA", title="Mr.A",
                          company="GenesysA",
                          address="Sredij pr.88A", home="11119", mobile="22229", work="33339", fax="44449",
                          email="a@mail.ru9",
                          email2="b@mail.ru9", email3="c@mail.ru9", homepage="www.home.ru9", byear="2001", ayear="2018",
                          address2="Moskovsky1", phone2="55559", notes="aaa9")


    old_contacts=db.get_contact_list()
    contact=random.choice(old_contacts)
    contact1.id=contact.id
    app.contact.mod_contact_by_id(contact.id,contact1)
    new_contacts=db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(contact)
    old_contacts.append(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts,key=Contact.id_or_max)==sorted(app.contact.get_contact_list(),key=Contact.id_or_max)

