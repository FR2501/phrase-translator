import os

from phrase_translator import __version__
from phrase_translator.dictionary_sources import (
    FileDictionarySource,
    WikiExtractDictionarySource,
    WordnetDictionarySource,
)
from phrase_translator.phrase_translator import PhraseTranslator
from phrase_translator.types import Language, Translation

source_language = Language.GERMAN
target_language = Language.ENGLISH


def test_version():
    assert __version__ == "0.1.1"


def test_phrase_translator_init():
    pt = PhraseTranslator(
        source_language=source_language, target_language=target_language
    )

    assert pt.translate_phrase("Test") == set()
    assert pt.translate_phrases(["Test", "Test"])


def test_file_dictionary_source():
    pt = PhraseTranslator()

    fds = FileDictionarySource(["tests/resources/test.dict"])
    pt.add_dictionary_source(fds)

    translations = pt.translate_phrase("Test")

    assert len(translations) == 1
    assert Translation("Test", "test", source_language, target_language) in translations


def test_wiki_dictionary_source():
    pt = PhraseTranslator()

    wds = WikiExtractDictionarySource(
        ["tests/resources/test_dump.json"], use_cached=False
    )
    pt.add_dictionary_source(wds)

    translations = pt.translate_phrase("Test")
    assert not translations

    translations = pt.translate_phrase("abietin")
    assert len(translations) == 2


def test_wordnet_dictionary_source():
    pt = PhraseTranslator()

    wds = WordnetDictionarySource()
    pt.add_dictionary_source(wds)

    translations = pt.translate_phrase("Test")
    assert translations
