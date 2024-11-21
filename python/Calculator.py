#Calculator Function

def convert_kilos_to_pounds(x):
    y = float(x)/2.205
    return y




def main():
    weight = input("Please input a weight in pounds:")

    new_weight = convert_kilos_to_pounds(weight)
    
    print(f"This is you converted weight {new_weight}")
    

if __name__ == "__main__":
    main()