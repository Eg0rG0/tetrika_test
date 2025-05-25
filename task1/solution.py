def strict(func):
    def wrapper(*args, **kwargs):
        vars_values = list(args) + list(kwargs.values())
        for (name, var_type), value in zip(func.__annotations__.items(), vars_values):
            if type(value) is not var_type:
                raise TypeError()
        res = func(*args, **kwargs)
        return res
    return wrapper
