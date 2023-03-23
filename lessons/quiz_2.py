def odd_and_even(list_1: list[int]) -> list[int]:
    i: int = 0
    new_list: list[int] = []
    while i < len(list_1):
        if list_1[i] % 2 != 0:
            new_list.append(list_1[i])
        i += 2
    return(new_list)

def value_exists(test_dict: dict[str,int], num: int) -> bool:
    in_dict: bool = False
    for elem in test_dict:
        if test_dict[elem] == num:
            in_dict == True
    return in_dict

def short_words(list1: list[str]) -> list[str]:
    new_list: list[str] = []
    for elem in list1:
        if len(elem) < 5:
            new_list.append(elem)
        else:
            print(f"{elem} is too long!")
    return new_list
            