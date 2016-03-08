def add(a,b):
    assert not (type(a) == str and type(b) == str), "strings"
    print a + b
    
add(2,"two")