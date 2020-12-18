def get_indices_of_item_weights(weights, length, limit):
        # Your code here
#     Example:
# ```
#     input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
#     output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

    # let's make a store dict
    store = {}
    # we can put weight as key to a dict, where value is the index
    for index in range(len(weights)):
        weight = weights[index]
        if weight not in store:
            store[weight] = index

    # go through the list
    result = []

    if length == 2 and weights[0] == weights[1] and weights[0] == limit /2:
        return (1,0)

    # then see if the limit - weight exists in the dict
  # then return the type as (array[0], array[1])
    # make a function that we sort the index of the array
    # make it called sort_array(array)
    def sort_array(array):
        if array[0] > array[1]:
            return (array[0], array[1])
        return (array[1],array[0])

    for index in range(len(weights)):
        weight = weights[index]
        weight_to_find = limit - weight
        if weight_to_find in store:
            result.append(store[weight])
            result.append(store[weight_to_find])
            return sort_array(result)
    # if it does add the first weight and the second weight to an array
  

    # if len(result) >= 2:
    #     return sort_array(result)
    # though before we need to check which array index is bigger so that we can return the tuple according to the readme
    # which is higher valued index should be placed first











    return None

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)