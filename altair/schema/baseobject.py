import json

import pandas as pd
import traitlets as T

from ..utils._py3k_compat import string_types

_attr_template = "Attribute not found: {0}. Valid keyword arguments for this class: {1}"


class BaseObject(T.HasTraits):

    skip = []

    def __init__(self, **kwargs):
        all_traits = list(self.traits())
        for k in kwargs:
            if k not in all_traits:
                raise KeyError(_attr_template.format(k, all_traits))
        super(BaseObject, self).__init__(**kwargs)

    def __contains__(self, key):
        try:
            value = getattr(self, key)
        except AttributeError:
            return False

        # comparison to None will break, so check DataFrame specifically
        if isinstance(value, pd.DataFrame):
            return True
        elif value is not None:
            if isinstance(value, (int, float, bool, string_types)):
                return True
            else:
                return bool(value)
        else:
            return False

    def __dir__(self):
        """Customize tab completed attributes."""
        return list(self.traits())+['to_dict', 'from_dict']

    @classmethod
    def from_dict(cls, dct):
        """Instantiate the object from a valid JSON dictionary

        Parameters
        ----------
        dct : dict
            The dictionary containing a valid JSON chart specification.

        Returns
        -------
        chart : Chart object
            The altair Chart object built from the specification.
        """
        # Import here to prevent circular imports
        from ..utils.visitors import FromDict
        return FromDict().clsvisit(cls, dct)

    @classmethod
    def from_json(cls, spec):
        """Instantiate the object from a valid JSON string

        Parameters
        ----------
        spec : string
            The string containing a valid JSON chart specification.

        Returns
        -------
        chart : Chart object
            The altair Chart object built from the specification.
        """
        return cls.from_dict(json.loads(spec))

    def to_dict(self, data=True):
        """Emit the JSON representation for this object as as dict.

        Parameters
        ----------
        data : bool
            If True (default) then include data in the representation.

        Returns
        -------
        spec : dict
            The JSON specification of the chart object.
        """
        from ..utils.visitors import ToDict
        self._finalize()
        return ToDict().visit(self, data)

    def to_json(self, data=True, sort_keys=True, **kwargs):
        """Emit the JSON representation for this object as a string.

        Parameters
        ----------
        data : bool
            If True (default) then include data in the representation.
        sort_keys : bool
            If True (default) then sort the keys in the output
        **kwargs
            Additional keyword arguments are passed to ``json.dumps()``

        Returns
        -------
        spec : string
            The JSON specification of the chart object.
        """
        return json.dumps(self.to_dict(data=data), sort_keys=True, **kwargs)

    def _finalize(self, **kwargs):
        """Finalize the object, and all contained objects, for export."""
        def finalize_obj(obj):
            if isinstance(obj, BaseObject):
                obj._finalize(**kwargs)
            elif isinstance(obj, list):
                for item in obj:
                    finalize_obj(item)

        for name in self.traits():
            value = getattr(self, name)
            finalize_obj(value)
