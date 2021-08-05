## WikiToJson

Convert a english wikipedia page to text, replicating the section hierarchy in json attributes.

## Instalation

    pip install wikitojson

## Basic Usage

    import wikitojson
    data = wikitojson.get("Computer")
    
    import json
    print(json.dumps(data, indent = 4))
