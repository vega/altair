
class Doc(dict):
    """Recursively constructed dottable dict"""
    def __init__(self, *args, **kwargs):
        super(Doc, self).__init__(*args, **kwargs)
        for k, v in self.items():
            try:
                self[k] = Doc(v)
            except (AttributeError, TypeError, ValueError):
                pass
        self.__dict__ = self
