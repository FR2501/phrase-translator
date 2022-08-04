from phrase_translator.types import Language, Translation


def test_language_equals():
    en = Language.ENGLISH
    de = Language.GERMAN

    assert en == en
    assert en == Language("en")
    assert de != en
    assert de != [1, 2, 3]


def test_translation_equals():
    translation1 = Translation("test", "Test", Language("en"), Language("de"))
    translation2 = Translation("Test", "test", Language("de"), Language("en"))

    assert translation1 == translation1
    assert translation1 != translation2
