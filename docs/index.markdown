---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

# layout: home
layout: default
---

**CityJSON** is the specification for _public transit_ data (stops, routes, timetables, etc)
and _mobility_ data (personal or shared scooters, bikes, cars, etc). It is an attempt
to improve and join two specifications [GTFS](https://developers.google.com/transit/gtfs/reference) and [GBFS](https://github.com/MobilityData/gbfs) into one.

# Folder structure
All files should be located in a folder or in a ZIP archive, and follow the structure:
```
agencies.json
agencies/
├── agency_foo.json
├── bar_agency.json
│   ...
└── another.json
stops.json
stops/
├── stop_foo.json
├── bar_stop.json
│   ...
└── another.json
routes.json
routes/
├── route_foo.json
├── bar_route.json
│   ...
└── another.json
...
```

Every entity could be presented either with another entities in the root JSON file
or separately in the own JSON file inside the corresponding entity's subfolder.
Depends on the data complexity, it could be presented only the root JSON file,
separately inside the corresponding entity's subfolder, or using both ways.

The main idea behind it, if entities are simple in terms of properties,
then they could be located in one file. But if any of entities has complex structure
or many properties, then it could be extracted into a separate file.

For example, below three options how data for agencies could be presented:
### Only root JSON file
agencies.json
```json
[
    {
        "id": "agency_foo",
        "name": "Foo Agency",
        "web": "https://foo.example.com"
    },
    {
        "id": "bar_agency",
        "name": "Bar Agency",
        "web": "https://bar.example.com"
    },
    {
        "id": "another",
        "name": "Another Agency",
        "web": "https://another.example.com"
    }
]
```


### Only inside entity's subfolder
agencies/agency_foo.json
```json
{
    "id": "agency_foo",
    "name": "Foo Agency",
    "web": "https://foo.example.com"
}
```

agencies/bar_agency.json
```json
{
    "id": "bar_agency",
    "name": "Bar Agency",
    "web": "https://bar.example.com"
}
```

agencies/another.json
```json
{
    "id": "another",
    "name": "Another Agency",
    "web": "https://another.example.com"
}
```


### Root JSON file and inside entity's subfolder
agencies.json
```json
[
    {
        "id": "agency_foo",
        "name": "Foo Agency",
        "web": "https://foo.example.com"
    },
    {
        "id": "bar_agency",
        "name": "Bar Agency",
        "web": "https://bar.example.com"
    }
]
```

agencies/another.json
```json
{
    "id": "another",
    "name": "Another Agency",
    "web": "https://another.example.com",
    "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAo0lEQVR4nO2TUQrCMBBE30cR/OmZvJifpb2Vd6kEv3qGSGURusnGtF1BsAMDy2Y2kwkJHPgLRAf+hsEWRIOXbxvcLIM99YwWmHQKPcDKOrLEVaconY6VCbIpvBMkKWoN4odap3ivebyiHEyDBuiAu7CTXmmTAXgofWKgOQprf7OlN8VnYY1JSZ8gZAaCcUVb9K/71JF7Rz0nGQrCQXpe+gMs8AQ318H4QPqjvwAAAABJRU5ErkJggg==",
    "loc": [52.5255170, 13.4153366]
}
```

# Entities
- [Agencies](./agencies.markdown)
- Stops
- Routes