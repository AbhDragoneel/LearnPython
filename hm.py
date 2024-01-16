def greeting(input):
    if "hello"  in input:
        return "Hello there!"
    else:
        return "I'm not sure what u mean"

greet = greeting("hello python")
print("hm, " + greet)