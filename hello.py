def greet(name):
    return f"Hello, {name}!"

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("GitHub") == "Hello, GitHub!"
    print("All tests passed!")

if __name__ == "__main__":
    test_greet()
