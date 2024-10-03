def count_apples(start_point, end_point, apple_tree, apples_list):
    """
    Print the number of apples that are between "start_point" and "end_point"
    
    Parameters:
    start_point (int): The starting point of the house.
    end_point (int): The ending point of the house.
    apple_tree (int): The position of the apple tree.
    apples_list (list): Distances at which apples fall from the tree.
    
    Returns:
    None
    """
    print(sum(1 for apple in apples_list 
              if start_point <= apple_tree + apple <= end_point))
    

def count_oranges(start_point, end_point, orange_tree, oranges_list):
    """
    Print the number of oranges that are between "start_point" and "end_point"
    
    Parameters:
    start_point (int): The starting point of the house.
    end_point (int): The ending point of the house.
    orange_tree (int): The position of the apple tree.
    oranges_list (list): Distances at which apples fall from the tree.
    
    Returns:
    None
    """
    print(sum(1 for orange in oranges_list
              if start_point <= orange_tree + orange <= end_point))

if __name__ == '__main__':
    start_point, end_point = map(int, input().split())
    apple_tree, orange_tree = map(int, input().split())
    _, _ = map(int, input().split())

    apples_list = list(map(int, input().split()))
    oranges_list = list(map(int, input().split()))

    count_apples(start_point, end_point, apple_tree, apples_list)
    count_oranges(start_point, end_point, orange_tree, oranges_list)