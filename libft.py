def ft_extract(users):
    extract1 = users.split("\n") 
    extract2 = []
    for i in range(len(extract1)):
        extract2.append(extract1[i].split(";"))
    return (extract2)

def ft_find(list, to_find):
    for i in range(len(list)):
        for x in range(len(list[i])):
            if list[i][x] == to_find:
                return (list[i])
    return (0)