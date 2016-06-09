"""{{ header }}"""

{% if objects %}
__all__ = [
          {%- for obj in objects %}
             "{{ obj.classname }}",{% endfor %}
          ]
{% endif %}

{% for obj in objects %}from .{{ obj.module }} import {{ obj.classname }}
{% endfor %}
