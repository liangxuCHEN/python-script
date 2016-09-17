def bread(func):
    
    def wrapper(*args, **kwargs):
        print "</''''''\>"
        func(*args, **kwargs)
        print "<\______/>"

    return wrapper


def ingredients(func):
    
    def wrapper(*args, **kwargs):
        print "#tomatoes#"
        func(*args, **kwargs)
        print "~salad~"
    
    return wrapper


@bread
@ingredients
def sandwitch(food='--ham--'):
    print food

sandwitch(food="meat")