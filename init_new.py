class VM:
    def __new__(cls, *args, **kwargs):
        print("Allocating resources...")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print(f"VM {self.name} initialized")

vm1 = VM("dev-server")
