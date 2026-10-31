"""Read the CURRENT DynamicFunctions/*.py sources for the Dash catalogue.

This module does not import generated code, use __pycache__, inspect Database/,
or cache previous results. Each call reloads the on-disk generated source.
The MainCreation dictionaries are generated snapshots; entries referring to
missing generated classes are filtered out.
"""
import ast
from pathlib import Path

DYNAMIC_ROOT = Path(__file__).resolve().parents[3] / 'DynamicFunctions'


def _generated_sources():
    """Return {class_name: (path, AST class)} for actual generated .py files."""
    classes = {}
    for path in sorted(DYNAMIC_ROOT.glob('*.py')):
        if path.name in ('MainCreation.py', 'FoldersPath.py'):
            continue
        tree = ast.parse(path.read_text(encoding='utf-8-sig'), filename=str(path))
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name == path.stem:
                classes[node.name] = (path, node)
    return classes


def _main_creation():
    path = DYNAMIC_ROOT / 'MainCreation.py'
    if not path.is_file():
        raise FileNotFoundError('Missing generated source: DynamicFunctions/MainCreation.py')
    tree = ast.parse(path.read_text(encoding='utf-8-sig'), filename=str(path))
    return next(n for n in tree.body
                if isinstance(n, ast.ClassDef) and n.name == 'MainCreation')


def _generated_dictionary(class_node, method, variable):
    """Read a literal dictionary in the generated source; never execute it."""
    for fn in class_node.body:
        if isinstance(fn, ast.FunctionDef) and fn.name == method:
            for stmt in fn.body:
                if isinstance(stmt, ast.Assign) and any(
                        isinstance(target, ast.Name) and target.id == variable
                        for target in stmt.targets):
                    return ast.literal_eval(stmt.value)
    return {}


def _object_definitions(main_class, classes):
    """Read object constructors from MainCreation.__init__ (generated source)."""
    objects = {}
    for fn in main_class.body:
        if not isinstance(fn, ast.FunctionDef) or fn.name != '__init__':
            continue
        for stmt in fn.body:
            if not (isinstance(stmt, ast.Assign) and len(stmt.targets) == 1
                    and isinstance(stmt.targets[0], ast.Attribute)
                    and isinstance(stmt.targets[0].value, ast.Name)
                    and stmt.targets[0].value.id == 'self'
                    and isinstance(stmt.value, ast.Call)
                    and isinstance(stmt.value.func, ast.Name)):
                continue
            class_name = stmt.value.func.id
            if class_name not in classes:  # Ignore organisations and absent modules.
                continue
            class_def = classes[class_name][1]
            ctor = next((x for x in class_def.body
                         if isinstance(x, ast.FunctionDef) and x.name == '__init__'), None)
            parameters = ([a.arg for a in ctor.args.args][1:] if ctor else [])
            arguments = {}
            for k, arg in zip(parameters, stmt.value.args):
                try:
                    arguments[k] = ast.literal_eval(arg)
                except (ValueError, TypeError, SyntaxError):
                    arguments[k] = (ast.unparse(arg) if hasattr(ast, 'unparse') else ast.dump(arg))
            # The last assignment to a self.attribute is the live one.
            objects[stmt.targets[0].attr] = {'class': class_name, 'attributes': arguments}
    return objects


def load_catalogue():
    """Re-read local generated source on EVERY call, returning current class hierarchy."""
    classes = _generated_sources()
    main_class = _main_creation()
    original = _generated_dictionary(main_class, 'getAllOrganisations', 'organisationDictionary')
    parent_details = _generated_dictionary(main_class, 'getAllWECs', 'wecMotherDictionaryALL')
    child_details = _generated_dictionary(main_class, 'getAllWECChildren', 'wecChildrenDictionary')
    objects = _object_definitions(main_class, classes)
    organisations = {}
    for name, value in original.items():
        wecs = {}
        for mother, children in value.get('WECs', {}).items():
            if mother not in classes:
                continue
            linked = {child: child_details.get(child, info)
                      for child, info in children.items()
                      if child in classes}
            wecs[mother] = {'details': parent_details.get(mother, {}).get('WEC class params', {}),
                            'children': linked}
        # Organisation instances exist as generated assignments in MainCreation.
        organisations[name] = {'information': value.get('organisationInfo', {}), 'wecs': wecs}
    return {'organisations': organisations, 'objects': objects,
            'generated_classes': sorted(classes)}


def generated_paths(_ignored_legacy_path=None):
    """Adapt the original navigation paths to the CURRENT generated class sources.

    The legacy positional path is intentionally ignored: no Database/ scan.
    """
    catalogue = load_catalogue()
    return {'name': 'DynamicFunctions', 'type': 'directory',
            'children': [{'name': name, 'type': 'directory', 'children': []}
                         for name in catalogue['organisations']]}
