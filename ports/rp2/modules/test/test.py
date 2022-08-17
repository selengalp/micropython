
def test():
    print("static function test")

class Test:
    def __init__(self):
        pass

    def test(self):
        print("instance method test")

def class_test():
    t = Test()
    t.test()
