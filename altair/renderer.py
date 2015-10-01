import traitlets as T

class Renderer(T.HasTraits):

    def render(self, **kwargs):
        raise NotImplementedError('This rendered is not fully implemented')
