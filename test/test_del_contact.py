from model.contact import Contact
import random
import time

def test_delete_some_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(
            Contact(firstname="Kirill", middlename="A", lastname="Zimin", nickname="kira", title="Mr.",
                    company="Genesys",
                    address="Sredij pr.88", home="1111", mobile="2222", work="3333", fax="4444", email="a@mail.ru",
                    email2="b@mail.ru", email3="c@mail.ru", homepage="www.home.ru", byear="2000", ayear="2017",
                    address2="Moskovsky", phone2="5555", notes="aaa"))
    old_contacts=db.get_contact_list()
    contact=random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    print(old_contacts)
    print(contact.id)
    time.sleep(5)
    new_contacts=db.get_contact_list()
    print(new_contacts)
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts==new_contacts
    if check_ui:
        assert sorted(new_contacts,key=Contact.id_or_max)==sorted(app.contact.get_contact_list(),key=Contact.id_or_max)

