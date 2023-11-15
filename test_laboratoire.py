import laboratoire
import pytest


@pytest.fixture 
def labo():
    return {'Simon':'F707', 'Pierre':'F808', 'Regis':'F101'}

def test_enrgistrer_arrivee(labo):
    laboratoire.enregistrer_arrivee(labo, 'Marc', 'F202')
    laboratoire.enregistrer_arrivee(labo, 'Luc', 'F303')
    laboratoire.enregistrer_arrivee(labo, 'Mathieu', 'F404')
    laboratoire.enregistrer_arrivee(labo, 'Juda', 'F505')
    assert laboratoire.est_presente(labo, 'Marc') == True

def test_est_presente(labo):
    assert not laboratoire.est_presente(labo, 'Luc') == True

def test_enrgistrer_depart(labo):
    laboratoire.enregistrer_depart(labo, 'Simon')
    assert laboratoire.est_presente(labo, 'Simon') == False

def test_modifier_bureau(labo):
    laboratoire.modifier_bureau(labo, 'Luc', 'F101')
    assert labo['Luc'] == 'F101'

def test_modifier_nom(labo):
    laboratoire.modifier_nom(labo, 'Regis', 'Paul')
    assert labo['Paul'] == 'F101'

 

if __name__ == '__main__':
    test_enrgistrer_arrivee(labo)
    test_enrgistrer_depart(labo)
    test_modifier_bureau(labo)
    test_modifier_nom(labo)