import os
import jinja2
import json
import numpy

def render(spec, width=None, height=None):
	
	from jinja2 import Template, escape

	if width is None:
		width = 500;
	if height is None:
		height = 300

	location = os.path.join(os.path.dirname(__file__), 'templates/template.html')
	base = open(location).read()
	d = spec.to_dict()
	d['config'] = {'width': width, 'height': height}

	class NumpyConvert(json.JSONEncoder):
		def default(self, obj):
			if isinstance(obj, numpy.generic):
				return numpy.asscalar(obj)
			return json.JSONEncoder.default(self, obj)

	spec = escape(json.dumps(d, cls=NumpyConvert))
	fields = {'spec': spec, 'width': width, 'height': height}
	t = Template(base)
	html = t.render(**fields)
	return html