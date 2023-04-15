# python3
# Aleksejs Šepeļevs, 221RDB494

def read_input():
    
    choice = input().strip()
    if choice == "I":
        model = input().strip()
        ievade = input().strip()
    elif choice == "F":
        fileName = "06"
        with open("tests/" + fileName, 'r') as file:
            model = file.readline().strip()
            ievade = file.readline().strip() 
    else:
        print("Wrong input")
        return
    return model, ievade

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(model, ievade):
 
    first = len(ievade)
    second = len(model)
    third = sum(ord(c) for c in model)
    index = []
    for i in range(first - second + 1):
        fourth = sum(ord(ievade[i + j]) for j in range(second))
        if third == fourth:
            if ievade[i : i + second] == model:
                index.append(i)
        else:
            continue        
    return index

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

