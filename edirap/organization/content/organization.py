from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from edirap.organization import MessageFactory as _

organization_types = SimpleVocabulary(
        [SimpleTerm(value=u'government', 
                    title=_(u'Government')),
        SimpleTerm(value=u'ngo', 
                   title=_(u'NGO')),
        SimpleTerm(value=u'private_sector', 
                   title=_(u'Private Sector')),
        SimpleTerm(value=u'academic', 
                   title=_(u'Academic/Research')),
        SimpleTerm(value=u'international', 
                   title=_(u'International Organization')),
        SimpleTerm(value=u'other', 
                   title=_(u'Other')),
         ])

organization_area= SimpleVocabulary(
        [SimpleTerm(value=u'policy', 
                    title=_(u'Policy')),
         SimpleTerm(value=u'regulatory', 
                    title=_(u'Regulatory')),
         ]
        )

economy = SimpleVocabulary(
    [SimpleTerm(value=u'AF',
                title=_(u'Afghanistan')),
    SimpleTerm(value=u'AU',
                title=_(u'Australia')),
    SimpleTerm(value=u'BD',
                title=_(u'Bangladesh')),
    SimpleTerm(value=u'BT',
                title=_(u'Bhutan')),
    SimpleTerm(value=u'BN',
                title=_(u'Brunei')),
    SimpleTerm(value=u'KH',
                title=_(u'Cambodia')),
    SimpleTerm(value=u'CN',
                title=_(u'China')),
    SimpleTerm(value=u'HK',
                title=_(u'Hong Kong')),
    SimpleTerm(value=u'IN',
                title=_(u'India')),
    SimpleTerm(value=u'ID',
                title=_(u'Indonesia')),
    SimpleTerm(value=u'IR',
                title=_(u'Iran')),
    SimpleTerm(value=u'JP',
                title=_(u'Japan')),
    SimpleTerm(value=u'LA',
                title=_(u'Lao PDR')),
    SimpleTerm(value=u'MO',
                title=_(u'Macao')),
    SimpleTerm(value=u'MY',
                title=_(u'Malaysia')),
    SimpleTerm(value=u'MV',
                title=_(u'Maldives')),
    SimpleTerm(value=u'MN',
                title=_(u'Mongolia')),
    SimpleTerm(value=u'MM',
                title=_(u'Myanmar')),
    SimpleTerm(value=u'NP',
                title=_(u'Nepal')),
    SimpleTerm(value=u'NZ',
                title=_(u'New Zealand')),
    SimpleTerm(value=u'KP',
                title=_(u'North Korea')),
    SimpleTerm(value=u'PK',
                title=_(u'Pakistan')),
    SimpleTerm(value=u'PH',
                title=_(u'Philippines')),
    SimpleTerm(value=u'SG',
                title=_(u'Singapore')),
    SimpleTerm(value=u'KR',
                title=_(u'South Korea')),
    SimpleTerm(value=u'LK',
                title=_(u'Sri Lanka')),
    SimpleTerm(value=u'TW',
                title=_(u'Taiwan')),
    SimpleTerm(value=u'TH',
                title=_(u'Thailand')),
    SimpleTerm(value=u'TL',
                title=_(u'Timor-Leste')),
    SimpleTerm(value=u'VN',
                title=_(u'Vietnam')),
    ]
    )

# Interface class; used to define content-type schema.

class IOrganization(form.Schema, IImageScaleTraversable):
    """
    Organizations
    """

    title = schema.TextLine(title=u'Name', 
                         description=u'Name of organization.')

    description = schema.TextLine(title=u'Description',
                                  description=u'Brief description '
                                  'of organization.'
                                  )

    organization_type = schema.Choice(
        title=_(u'Organization Type'),
        vocabulary = organization_types,
    )
