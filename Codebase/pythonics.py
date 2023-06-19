import threading

def my_thread(condition):
    while True:
        # Code inside the loop
        if condition[0]:
            print("Condition is True")
        else:
            print("Condition is False")

def main():
    condition = [True]  # Use a list to make it mutable

    thread = threading.Thread(target=my_thread, args=(condition,))
    thread.start()

    # Changing the condition while the loop is running
    # This will affect the behavior of the loop
    condition[0] = False

    thread.join()

if __name__ == "__main__":
    main()
