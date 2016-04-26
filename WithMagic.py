
class systemresource:
    def __enter__(self):
        print("enter, open resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit, clean up resource")
        print("exc_type", exc_type)
        print("exc_val", exc_val)
        print("exc_tb", exc_tb)

    def do_something(self):
        1/0

with systemresource() as r:
    print("res:", r)
    r.do_something()
