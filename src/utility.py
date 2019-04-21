import os
import json
import importlib


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_modules():
    files = os.listdir('commands')
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def load_module(module_name):
    try:
        importlib.import_module('commands.{}'.format(module_name))
    except ModuleNotFoundError:
        pass
