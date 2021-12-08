from enrichforall import E4ALangDetect


def test_english():
    ld = E4ALangDetect('This is English. Got it or do you need more?')
    assert ld.lang_id() == 'English'


def test_romanian():
    ld = E4ALangDetect('Cum e mai bine să-mi protejez familia de COVID-19?')
    assert ld.lang_id() == 'Romanian'


def test_german():
    ld = E4ALangDetect(
        'Neuer Look für Euro-Scheine bis 2024: Haben Sie eine Design-Idee?')
    assert ld.lang_id() == 'German'


def test_french():
    ld = E4ALangDetect(
        "L'Euro a bientôt 20 ans, et pour l'occasion un nouveau look... pour 2024 au mieux.")
    assert ld.lang_id() == 'French'


def test_luxembourgish():
    ld = E4ALangDetect(
        'Déi italienesch Pompjeeën hunn bei dësem Onwieder een Affer ze bekloen.')
    assert ld.lang_id() == 'Luxembourgish'


def test_danish():
    ld = E4ALangDetect(
        'Vi bruger cookies til at optimere brugeroplevelsen og målrette indholdet på Udenrigsministeriets hjemmesider.')
    assert ld.lang_id() == 'Danish'
