# -*- coding: utf-8 -*-

from wtforms import Form
from wtforms import TextField, TextAreaField, BooleanField
from wtforms import DecimalField, FileField, IntegerField, RadioField
from wtforms import SelectMultipleField
from wtforms import validators

from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from collective.wtforms.views import WTFormView
from collective.wtforms.views import WTFormControlPanelView

from example.wtforms import messageFactory as _

class Form1(Form):
    one = TextField("Field One", [validators.required()])
    two = TextField("Field Two")
    three = TextField("Field Three")

class Form1View(WTFormView):
    formClass = Form1
    buttons = ('Create', _(u'Cancel'))
    #label = _(u'Form 1')

    def submit(self, button):
        if button == 'Create' and self.validate():
            # do fun stuff here
            self.context.value = self.form.one.data


class VocabularyWrapper(object):
    
    def __init__(self, vocabulary_name=u'', i18n_domain='plone'):
        self.vocabulary_name = vocabulary_name
        self.i18n_domain = i18n_domain
    
    def __iter__(self):
        site = getSite()        
        vocabulary = getUtility(IVocabularyFactory, name=self.vocabulary_name)
        translation_service = getToolByName(site, 'translation_service')
        terms = vocabulary(site)
        for term in terms:
            yield (term.value,
                   translation_service.utranslate(domain=self.i18n_domain,
                                                  msgid=term.token,
                                                  default=term.token,
                                                  context=site)
                   )
        

class Form2(Form):    
    one = TextField(_(u"Field One"), [validators.required()])
    two = TextAreaField("Field Two", description=_(u"Help text of field 2"))
    three = TextField("Field Three")
    four = BooleanField("Field four", default=True)
    five = DecimalField("Field Five", description="This is a decimal field")
    six = FileField("Field six")
    seven = IntegerField("Field seven", description="Integer there", default=7)
    eight = RadioField("Field eight", default='a2', choices=VocabularyWrapper('example.wtforms.test_vocabulary',
                                                                              i18n_domain='example.wtforms'))

class Form2View(WTFormView):
    formClass = Form2
    #buttons = ('Create', _(u'Cancel'))
    label = _(u'Form 2')
    description = _(u'this is form 2!')
    fieldsets = (
        (_(u'Fieldset One'), ('one', 'two', 'five', 'eight')),
        ('Fieldset Two', ('three', 'four', 'six', 'seven'))
    )

    def submit(self, button):
        if button == 'Save' and self.validate():
            # do fun stuff here
            self.context.value = self.form.one.data
            print self.form.five.data


class Form3(Form):
    one = SelectMultipleField("Field one", choices=VocabularyWrapper('plone.app.vocabularies.Roles',
                                                                     i18n_domain='plone'))
    two = TextField("Field Two")

class Form3View(WTFormControlPanelView):
    formClass = Form3
    label = _(u'Form 3')
    buttons = ('Save', 'Cancel')
    fieldsets = (
        (_(u'Fieldset One'), ('one',)),
        ('Fieldset Two', ('two',))
    )

    def submit(self, button):
        if button == 'Save' and self.validate():
            # do fun stuff here
            self.context.value = self.form.one.data
