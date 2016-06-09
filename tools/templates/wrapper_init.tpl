"""{{ header }}"""

{% if objects %}
__all__ = [
          {%- for obj in objects %}
             "{{ obj.name }}",{% endfor %}
          ]
{% endif %}

{% for obj in objects %}from .{{ obj.root }} import {{ obj.name }}
{% endfor %}
