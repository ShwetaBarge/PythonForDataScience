def printProps(props, name, var):
    """
        utils.printProps((type, id, callable, len, sys.getrefcount), 'a', a)
    """   
    w = len(max([p.__name__ for p in props], key=len))
    for p in props:
        try:
            print("{:>{width}}({}) : {}".format(p.__name__, name, p(var), width=w))
        except TypeError:
            print("{:>{width}}({}) : {}".format(p.__name__, name, "cannot be called", width=w))