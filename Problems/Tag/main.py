def tagged(func):
    def wrapper(arg):
        return f"<title>{arg.strip()}</title>"

    return wrapper
