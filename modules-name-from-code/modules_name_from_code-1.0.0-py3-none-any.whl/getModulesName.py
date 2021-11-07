def get_modules(buildFilePath: str, sort: bool = False):

    file = open(buildFilePath, "r", encoding = 'UTF-8')
    code = file.read()
    file.close()

    codeLine = code.split("\n")

    codeModules = []

    for line in codeLine:

        # Remove comments
        if line.find("#") != -1:
            line = line[:line.find("#")]

        lineSplit = line.split(" ")
        if "import" in lineSplit:

            # for moduleName import ~~~
            if "from" in lineSplit:
                # from "module" import ~~~
                codeModules.append(lineSplit[lineSplit.index("from") + 1])

            # import module
            # import module, moduleName, ~~~
            # import module,moduleName,~~~
            else:
                # Delete "import"
                lineSplit.remove("import")

                for module in lineSplit:
                    module = module.split(",")

                for moduleName in module:
                    codeModules.append(moduleName)

    # Deduplication
    # Sort in order
    if sort:
        codeModules = dict.fromkeys(codeModules)
        codeModules = list(codeModules)
    # Randomly
    else:
        codeModules = set(codeModules)
        codeModules = list(codeModules)

    # Sort
    if sort:
        codeModules.sort

    return codeModules