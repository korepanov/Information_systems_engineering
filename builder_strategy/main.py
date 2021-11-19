from strategy import *
from builder import * 
        
if __name__ == "__main__":
    builder = ConcreteBuilder()
    builder.produce_solt()
    builder.produce_flour()
    builder.bread.list_parts()

    context = Context(MakeBlackBread)
    print("Black bread:")
    context.make_bread(4)
    context.strategy = MakeWhiteBread
    print("White bread:")
    context.make_bread(7)
