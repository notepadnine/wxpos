import pos
import imp, os, sys

def loadModules():
    print '*Loading modules...'
    #import pos.modules
    #modules_path = pos.modules.__path__[0]
    modules_path = os.path.dirname(__file__)

    modules = []
    sys.path.insert(0, modules_path)
    for name in os.listdir(modules_path):
        full_path = os.path.join(modules_path, name)
        if os.path.isdir(full_path):
            if name.startswith('.'):
                print '*Ignored module', name
                continue
            try:
                _file, pathname, description = imp.find_module(name)
            except ImportError:
                print '*Invalid module', name
            else:
                module = imp.load_package(name, pathname)
                modules.append(module)
    sys.path.remove(modules_path)
    modules.sort(cmp=dependencyCmp)
    print '*(%d) modules found: %s' % (len(modules), ', '.join([m.__name__ for m in modules]))
    return modules

def checkDependencies():
    print '*Checking module dependencies...'
    module_names = map(lambda m: m.__name__, modules)
    for top in modules:
        missing = filter(lambda dep: dep not in module_names, top.dependencies)
        if len(missing)>0:
            print '*** Missing dependencies for module', top.__name__, ':', ' '.join(missing)
            raise Exception, 'Missing dependency'

def dependencyCmp(m1, m2):
    if m1.__name__ in m2.dependencies and m2.__name__ in m1.dependencies:
        return 0
    elif m2.__name__ in m1.dependencies:
        return 1
    elif m1.__name__ in m2.dependencies:
        return -1
    else:
        return 0

def isInstalled(module_name):
    return (module_name in [top.__name__ for top in modules])

modules = loadModules()
checkDependencies()

def configDB(test):
    print '*Clearing database...'
    pos.db.clear()
    for top in modules:
        try:
            config = top.configDB
        except AttributeError:
            print '*DB Config missing', top.__name__
        else:
            print '*Configuring', top.__name__
            config(test)

def extendMenu(menu):
    items = []
    for top in modules:
        try:
            item = top.ModuleMenu
        except AttributeError:
            print '*Menu Extension missing', top.__name__
        else:
            items.append(item(menu))

    for item in items:
        item.loadSubItems()
