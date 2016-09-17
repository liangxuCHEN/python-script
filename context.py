import contextlib

@contextlib.contextmanager
def make_context():
    print 'entering'
    try:
        yield {'xdeoodj'}
    except RuntimeError, err:
    	print "Error:" , err
    finally:
        print 'exiting'

print 'Noraml'

with make_context() as value:
    print 'inside with statement', value

print 'Handle error'
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print 'Unhandl erro'
with make_context() as value:
    raise ValueError('this exception is not handle')

"""
class Context(object):
    def __init__(self):
        print 'init'
    def __enter__(self):
        print '__enter__'
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        print 'exit'

with Context():
	print "Doing work"
"""
