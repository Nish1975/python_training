
def test_mod_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.mod_first_contact()
    app.session.logout()

