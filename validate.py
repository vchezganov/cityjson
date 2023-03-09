import pathlib
import json
import jsonschema


def validate_examples(entity_name: str):
    # path_root = pathlib.Path().resolve()
    # resolver = jsonschema.validators.RefResolver(base_uri=f'{path_root.as_uri()}/',
    #                                              referrer=True)

    # resolver = jsonschema.validators.RefResolver(base_uri='https://github.com/vchezganov/cityjson/',
    #                                              referrer=True)

    folder_schema = pathlib.Path('schema')

    with open(folder_schema / 'definitions.json', mode='r') as fin:
        definition_schema = json.load(fin)

    with open(folder_schema / f'{entity_name}.json', mode='r') as fin:
        entity_schema = json.load(fin)

    store = {
        definition_schema['$id']: definition_schema,
        entity_schema['$id']: entity_schema,
    }

    resolver = jsonschema.RefResolver(base_uri='https://github.com/vchezganov/cityjson/schema/',
                                      referrer=True,
                                      store=store)

    folder_examples = pathlib.Path('examples') / entity_name
    for path_example in folder_examples.iterdir():
        if not path_example.is_file():
            continue

        with open(path_example, mode='r') as fin:
            example = json.load(fin)

        jsonschema.validate(example, schema=entity_schema, resolver=resolver)
        # jsonschema.validate(example, schema={'$ref': f'{entity_name}.json'}, resolver=resolver)


if __name__ == '__main__':
    for entity_name in ('settings', 'agencies', 'stops', 'routes'):
        validate_examples(entity_name)
