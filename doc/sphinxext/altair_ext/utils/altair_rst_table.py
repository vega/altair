"""
Utility for creating an rst table for documenting altair objects
"""
import six

import traitlets
from traitlets.utils.importstring import import_item

from altair.api import TopLevelMixin
try:
    # Altair > 1.2
    from altair.schema._interface import named_channels, channel_collections
except:
    # Altair <= 1.2
    from altair.schema._wrappers import named_channels, channel_collections

__all__ = ['altair_rst_table']


# This holds info for how to build links to the Vega-Lite documentation
VEGALITE_DOC_URL = 'http://vega.github.io/vega-lite/docs/'
VEGALITE_DOC_PAGES = {'config': 'config.html#top-level-config',
                      'cellconfig': 'config.html#cell-config',
                      'markconfig': 'config.html#mark-config',
                      'scaleconfig': 'config.html#scale-config',
                      'axisconfig': 'config.html#axis-config',
                      'legendconfig': 'config.html#legend-config',
                      'facetconfig': 'config.html#facet-config'}

for attr in ['data', 'transform', 'mark', 'encoding', 'aggregate', 'bin',
             'sort', 'timeunit', 'scale', 'axis', 'legend']:
    VEGALITE_DOC_PAGES[attr] = attr + '.html'

for channel in ['color', 'column', 'detail', 'opacity', 'order', 'path',
                'row', 'shape', 'size', 'text', 'x', 'y']:
    VEGALITE_DOC_PAGES[channel] = 'encoding.html#def'


def _get_trait_info(name, trait):
    """Get a dictionary of info for an object trait"""
    type_ = trait.info()
    help_ = trait.help

    if isinstance(trait, traitlets.List):
        trait_info = _get_trait_info('', trait._trait)
        type_ = 'list of {0}'.format(trait_info['type'])
    elif isinstance(trait, traitlets.Enum):
        values = trait.values
        if all(isinstance(val, str) for val in values):
            type_ = 'string'
            help_ += ' One of {0}.'.format(values)
    elif isinstance(trait, traitlets.Union):
        trait_info = [_get_trait_info('', t) for t in trait.trait_types]
        type_ = ' or '.join(info['type'] for info in trait_info)
        help_ += '/'.join([info['help'] for info in trait_info
                           if info['help'] != '--'])
    elif isinstance(trait, traitlets.Instance):
        cls = trait.klass
        if isinstance(cls, six.string_types):
            cls = import_item(cls)
        if issubclass(cls, traitlets.HasTraits):
            type_ = ':class:`~altair.{0}`'.format(cls.__name__)

    type_ = type_.replace('a ', '')
    type_ = type_.replace('unicode string', 'string')
    return {'name': name, 'help': help_ or '--', 'type': type_ or '--'}


def _get_category(obj):
    """Get the category of an altair object"""
    name = obj.__name__

    if 'Chart' in name:
        return (0, 'Top Level Objects')
    elif name in dir(named_channels):
        return (2, 'Encoding Channels')
    elif name in dir(channel_collections):
        # out of order because encoding channels also appear here
        return (1, 'Channel Collections')
    elif 'Config' in name:
        return (3, 'Config Objects')
    else:
        return (4, 'Other Objects')


def _get_object_info(obj):
    """Get a dictionary of info for an object, suitable for the template"""
    D = {}
    name = obj.__name__
    D['name'] = name

    if name.lower() in VEGALITE_DOC_PAGES:
        url = VEGALITE_DOC_URL + VEGALITE_DOC_PAGES[name.lower()]
        D['description'] = ("(See also Vega-Lite's Documentation for "
                            "`{0} <{1}>`_)".format(name, url))

    D['traits'] = [_get_trait_info(name, trait)
                   for name, trait in sorted(obj.class_traits().items())]

    D['category'] = _get_category(obj)

    return D

def altair_rst_table(obj, columns=None, title_map=None,
                     include_description=False):
    obj_info = _get_object_info(obj)
    columns = columns or ['name', 'type', 'help']
    title_map = title_map or {'name':'Trait', 'type':'Type',
                              'help':'Description'}

    rows = [[trait[column] for column in columns]
            for trait in obj_info['traits']]
    titles = [title_map.get(column, column) for column in columns]
    lengths = [[len(item) for item in row] for row in rows]
    maxlengths = [max(col) for col in zip(*lengths)]

    def pad(row, fill=' '):
        return '  '.join(item.ljust(length, fill)
                         for item, length in zip(row, maxlengths))

    div = pad(['', '', ''], fill='=')

    lines = ['']
    if include_description and 'description' in obj_info:
        lines.extend([obj_info['description'], ''])
    lines.extend(['', div, pad(titles), div])
    lines.extend(map(pad, rows))
    lines.extend([div, '', ''])

    return lines
