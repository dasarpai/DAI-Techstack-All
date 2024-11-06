import numpy as np

def print_numbers():
    ar1 = np.array(range(1,20,2))
    ar2 = np.array(range(20,1,-2))
    result = ar1*ar2 

    for i in result:
        print(i)

if __name__ == "__main__":
    print_numbers()