def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    d=list_num[0]
    b=list_num[-1]
    if d>b:
        i=d
    else:
        i=b
    return i
print(main([9,2,5,4,8,6,32,]))
