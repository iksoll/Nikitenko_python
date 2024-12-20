def group_symbols(input_string):
    symbols = input_string.split()
    
    grouped = []
    
    current_group = [symbols[0]]
    
    for i in range(1, len(symbols)):
        if symbols[i] == symbols[i - 1]:
            current_group.append(symbols[i])
        else:
            grouped.append(current_group)
            current_group = [symbols[i]]

    grouped.append(current_group)
    
    return grouped

input_data = "с с с о о о с с и и и и с к к к а а а а а"

print(group_symbols(input_data))
