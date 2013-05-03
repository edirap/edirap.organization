from collective.grok import gs
from edirap.organization import MessageFactory as _

@gs.importstep(
    name=u'edirap.organization', 
    title=_('edirap.organization import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('edirap.organization.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
