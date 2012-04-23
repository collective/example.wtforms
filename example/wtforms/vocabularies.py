# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from example.wtforms import messageFactory as _

class TestVocabulary(object):
    """Vocabulary factory for testing.
    """
    implements( IVocabularyFactory )

    def __call__(self, context):
        elems = (('a1', _(u"Choice 1")), ('a2', _(u"Choice 2")),
                 ('a3', _(u"Choice 3")), ('a4', _(u"Choice 4")))
        terms = [SimpleTerm(elem[0],elem[1]) for elem in elems]
        return SimpleVocabulary(terms)

TestVocabularyFactory = TestVocabulary()