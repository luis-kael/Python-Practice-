def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
    
hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")

hello("Hello", title="Mr.", last="John", first="James")

for x in range(1,11):
    print(x, end=" ")