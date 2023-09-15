import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple Python script with a command-line argument.")
    parser.add_argument("value", type=int, help="An integer value to be passed as an argument.")
    
    args = parser.parse_args()
    value = args.value
    
    # Your logic using the passed argument goes here
    result = value * 2
    
    print(f"The result of doubling the value {value} is {result}.")

if __name__ == "__main__":
    main()
