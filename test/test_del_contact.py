from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(
            Contact(firstname="Kirill", middlename="A", lastname="Zimin", nickname="kira", title="Mr.",
                    company="Genesys",
                    address="Sredij pr.88", home="1111", mobile="2222", work="3333", fax="4444", email="a@mail.ru",
                    email2="b@mail.ru", email3="c@mail.ru", homepage="www.home.ru", byear="2000", ayear="2017",
                    address2="Moskovsky", phone2="5555", notes="aaa"))

    old_contacts=app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts=app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[index:index+1]=[]
    assert old_contacts==new_contacts
