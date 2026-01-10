import threading
import time

def take_order():
    try:
        print("Taking Order...")
        time.sleep(2)
        print("Order Taken.")
    except Exception as e:
        print(f"Error in taking order: {e}")

def prepare_food():
    try:
        print("Preparing Food...")
        time.sleep(4)
        print("Food Prepared.")
    except Exception as e:
        print(f"Error in preparing food: {e}")

def serve_food():
    try:
        print("Serving Food...")
        time.sleep(1)
        print("Food Served.")
    except Exception as e:
        print(f"Error in serving food: {e}")

# Main Program
try:
    order_thread = threading.Thread(target=take_order)
    prepare_thread = threading.Thread(target=prepare_food)
    serve_thread = threading.Thread(target=serve_food)

    order_thread.start()
    prepare_thread.start()
    serve_thread.start()

    order_thread.join()
    prepare_thread.join()
    serve_thread.join()

    print("All tasks completed!")

except Exception as e:
    print(f"Unexpected error in thread management: {e}")
