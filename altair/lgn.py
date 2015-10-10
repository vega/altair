from .renderer import Renderer

from lightning import Lightning


lgn = Lightning(ipython=True, local=True)


class LightningRenderer(Renderer):
    
    def render(self, spec, **kwargs):
        return lgn.vega_lite(spec.to_dict())

