import app
import pytest

docs = [
    ('2207 876234', 'Василий Гупкин'),
    ('11-2', 'Геннадий Покемонов'),
    ('10006', 'Аристарх Павлов'),
]

shelf = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('10006', '2'),
    ('5455 028765', '1'),
]

add_doc = [
    ('Q','D','F', '3'),
    ('QQ','DD','FF','2'),
    ('QQQ','DDD','FFF','1')
]

dropDoc = [('Q'),('QQ'),('QQQ')]

shelf_add = [
    (5),(6),(159),(598),
]

modify = [
    ('2207 876234', 598),
    ('11-2', 6),
    ('10006', 159),
]



@pytest.mark.parametrize("number_doc, result", docs)
def test_search_people(number_doc, result):
    res = app.search_people(number_doc)
    assert res == result

@pytest.mark.parametrize("number_doc, result", shelf)
def test_search_shelf(number_doc, result):
    res = app.search_shelf(number_doc)
    assert res == result

def test_search_list():
    res = app.search_list()
    assert isinstance(res, list)

@pytest.mark.parametrize("number_doc, type_doc, owner, shelf", add_doc)
def test_add_doc(number_doc, type_doc, owner, shelf):
    res = app.add_doc(number_doc, type_doc, owner, shelf)
    assert res == True

@pytest.mark.parametrize("number_doc", dropDoc)
def test_drop_doc(number_doc):
    res = app.drop_doc(number_doc)
    assert res == True

@pytest.mark.parametrize("shelf", shelf_add)
def test_add_shelf(shelf):
    res = app.add_shelf(shelf)
    assert res == True

@pytest.mark.parametrize("number_doc, shelf", modify)
def test_modify_doc(number_doc, shelf):
    res = app.modify_doc(number_doc, shelf)
    assert res == True