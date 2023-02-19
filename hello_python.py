import turtle

def printHello():
    A = "World"
    print(f"hello,{A}")

if __name__ == "__main__":
    printHello()
    
    turtle.pensize(8)
    turtle.pencolor('yellow')

    turtle.forward(100)
    turtle.right(60)
    turtle.forward(100)
    turtle.right(80)

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

    turtle.mainloop()