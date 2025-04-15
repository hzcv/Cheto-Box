import uuid

def generate_key():
    prefix = "CB01Days-"
    unique_id = uuid.uuid4()
    return f"{prefix}{unique_id}"

def main():
    try:
        count = int(input("How many keys should I generate? "))
        if count < 1:
            print("Please enter a number greater than 0")
            return
            
        print("\nGenerated keys:")
        for _ in range(count):
            print(generate_key())
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
