"""{{ header }}"""

{% if objects %}
__all__ = [{% for object in objects %}
             "{{ object }}",{% endfor %}
          ]
{% endif %}

{% for object in objects %}from .{{ object.lower() }} import {{ object }}
{% endfor %}
