def subset_sum_problem_help(number, hashed_array, hash_store, used):
    if (number == 0):
        hash_store[tuple(used)] = used
    elif(number > 0):
        for each in hashed_array:
            print(hash_store)
            for i in range(int(hashed_array[each])):
                new_hashed_array = hashed_array.copy()
                new_hashed_array[each] -= 1

                new_num = number - each
                subset_sum_problem_help(new_num, new_hashed_array, hash_store, used + [each])


def subset_sum_problem(arr, num):
    hash_store = {}
    hashed_array = {}
    for each in arr:
        if(each not in hashed_array):
            hashed_array[each] = 1
        else:
            hashed_array[each] += 1

    subset_sum_problem_help(num, hashed_array, hash_store, [])

    return list(hash_store.values())


print(subset_sum_problem([-3,1,1,1,5],5))
