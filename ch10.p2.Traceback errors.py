def spam():
    bacon()
def bacon():
    raise Exception('This is error message')

spam()
