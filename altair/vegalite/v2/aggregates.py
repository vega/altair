from .schema import core as _schema_core
from .schema import Undefined
from altair.utils import core as _utils_core


class _AggregateFunction(object):
    _doc_template = """Altair {aggregate} aggregate

    {aggregate}(field, type='quantitative', **kwargs)

    Parameters
    ----------
    field : string
        the name of the field to be aggregated
    type : string, default='quantitative'
        the type of the aggregated field
    **kwargs :
        additional parameters are added to the dict

    Returns
    -------
    dct : dictionary
        dictionary with keys "aggregate", "field", and "type"
    """
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.__doc__ = self._doc_template.format(aggregate=aggregate)

    def __call__(self, field=Undefined, type='quantitative'):
        type = _utils_core.INV_TYPECODE_MAP.get(type, type)
        if field is Undefined and self.aggregate != 'count':
            raise TypeError("{0}() missing 1 required positional argument: 'field'".format(self.aggregate))
        if type not in _utils_core.TYPECODE_MAP:
            valid = list(_utils_core.TYPECODE_MAP) + list(_utils_core.INV_TYPECODE_MAP)
            raise ValueError("invalid type argument '{0}'; must be one of {1}".format(type, valid))
        dct = {'aggregate': self.aggregate}
        if field is not Undefined:
            dct['field'] = field
        if type is not Undefined:
            dct['type'] = type
        return dct


# Define an object for each valid aggregate
__all__ = _schema_core.Aggregate.resolve_references()['enum']

for aggregate in __all__:
    globals()[aggregate] = _AggregateFunction(aggregate)
