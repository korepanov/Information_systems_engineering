from strategy_iterator import *

if __name__ == "__main__":
    context = Context(MakeBlackBread, 5)

    print(next(context))
    print(next(context))
    print(next(context))

    context.strategy = MakeWhiteBread

    print(next(context))
    print(next(context))