---
layout: default
title: Agency Entity
permalink: /agencies
---

**Agency** entity presents information about certain provider. It could be
a bus operator, a rail agency, or a mobility provider for shared vehicles.

## Examples
{% for ex in site.static_files %}
  {% if ex.path contains 'examples/agencies' %}
```json
{% include_relative {{ ex.path }} -%}
```
  {% endif %}
{% endfor %}



## Structure
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/product.schema.json",
  "title": "Agency",
  "type": "object",
  "properties": {
    "id": {
      "description": "The unique identifier for an agency",
      "type": "string"
    },

    "name": {
      "description": "Name of the agency",
      "type": "string"
    },

    "description": {
      "description": "Description of the agency",
      "type": "string"
    },

    "web": {
      "description": "Website of the agency",
      "type": "string"
    },

    "phone": {
      "description": "Phone of the agency",
      "type": "array",
      "items": {
        "type": "object",
        "propeties": {
            "phone_type": {
                "description": "Type of the phone (support, information, etc)",
                "type": "string"
            }

            "number": {
                "description": "Phone number",
                "type": "string"
            }
        },
        "required": [ "phone_type", "number" ]
      }
    },

    "email": {
      "description": "Email of the agency",
      "type": "string"
    },

    "timezone": {
      "description": "Timezone where the agency operates and that is used for timetables",
      "type": "string"
    }
  },

  "required": [ "id", "name" ]
}
```
