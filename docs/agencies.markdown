---
layout: default
title: Agency Entity
permalink: /agencies
---

**Agency** entity presents information about certain provider. It could be
a bus operator, a rail agency, or a mobility provider for shared vehicles.

# Examples
{% for ex in site.static_files %}
  {% if ex.path contains 'examples/agencies' %}
## #{{ forloop.index }}
```json
{% include_relative {{ ex.path }} -%}
```
  {% endif %}
{% endfor %}


# Description
<table>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>

<tr>
<td>id</td>
<td>string / required</td>
<td>Unique identifier of the agency. All agency identifiers must be unique within the dataset.</td>
</tr>

<tr>
<td>name</td>
<td>string / required</td>
<td>Name of the agency.</td>
</tr>

<tr>
<td>description</td>
<td>string / required</td>
<td>Description of the agency.</td>
</tr>

<tr>
<td>web</td>
<td>string / required</td>
<td>Website of the agency.</td>
</tr>

<tr>
<td>phone</td>
<td>string / required</td>
<td markdown="1">
Phone of the agency. It could be only one phone number that is marked as `main` by default:
```json
"phone": "+1234567"
```
Or it could be multiple phone numbers of different types:
```json
"phone": [
  {"phoneType": "main", "value": "+1234567"},
  {"phoneType": "support", "value": "+1234568"}
]
```
</td>
</tr>

<tr>
<td>email</td>
<td>string / required</td>
<td markdown="1">
Email of the agency. It could be only one email address that is marked as `main` by default:
```json
"email": "main@agency.com"
```
Or it could be multiple email addresses of different types:
```json
"email": [
  {"emailType": "main", "value": "main@agency.com"},
  {"emailType": "support", "value": "support@agency.com"}
]
```
</td>
</tr>

<tr>
<td>timezone</td>
<td>string / required</td>
<td>Timezone of the agency. All times in timetables belonging to the agency must be in the agency's timezone.</td></tr>

<tr>
<td>loc</td>
<td>string / required</td>
<td>Location of the agency.</td></tr>
</table>


# Schema
```json
{% include_relative data/schema/agencies.json -%}
```
