# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Kirill", middlename="A", lastname="Zimin", nickname="kira", title="Mr.", company="Genesys",
                                address="Sredij pr.88", home="1111", mobile="2222", work="3333", fax="4444", email="a@mail.ru",
                                email2="b@mail.ru", email3="c@mail.ru", homepage="www.home.ru", byear="2000", ayear= "2017", address2="Moskovsky", phone2="5555", notes="aaa"))
    app.session.logout()
