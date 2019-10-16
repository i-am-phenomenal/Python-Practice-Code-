import threading

def dummy_function():
    print(" I am here")

def another_function():
    print("I am in Thread 2")

thread = threading.Thread(target = dummy_function, args = ())
thread.start()

thread2 = threading.Thread(target = another_function, args = ())
thread2.start()
