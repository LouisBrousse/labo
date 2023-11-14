import laboratoire

import pytesteponse = est


labo = {'Simon':'F707', 'Pierre':'F808', 'Regis':'F101'}




def test_enrgistrer_arrivee():
    laboratoire.enregistrer_arrivee(labo, 'Marc', 'F202')
    laboratoire.enregistrer_arrivee(labo, 'Luc', 'F303')
    laboratoire.enregistrer_arrivee(labo, 'Mathieu', 'F404')
    laboratoire.enregistrer_arrivee(labo, 'Juda', 'F505')
    assert laboratoire.est_presente(labo, 'Marc') == True

def test_est_presente():
    assert not laboratoire.est_presente(labo, 'Luc') == False

def test_enrgistrer_depart():
    laboratoire.enregistrer_depart(labo, 'Simon')
    assert laboratoire.est_presente(labo, 'Simon') == False

def test_modifier_bureau():
    laboratoire.modifier_bureau(labo, 'Luc', 'F101')
    assert labo['Luc'] == 'F101'

def test_modifier_nom():
    laboratoire.modifier_nom(labo, 'Marc', 'Paul')
    assert labo['Paul'] == 'F202'

 

if __name__ == '__main__':
    test_enrgistrer_arrivee(labo)
    test_enrgistrer_depart(labo)
    test_modifier_bureau(labo)
    test_modifier_nom(labo)