def _order_crossover_calculator(parent_1: list[int], parent_2: list[int], first_cut: int, second_cut: int) -> list[int]:
    length = len(parent_1)
    new_order = [0 for _ in range(length)]
    segment = parent_1[first_cut:second_cut]
    new_order[first_cut:second_cut] = segment

    i = second_cut  # pointer in new_order
    j = second_cut  # pointer in parent_2
    for _ in range(length):
        if parent_2[j] not in segment:
            new_order[i] = parent_2[j]
            i = (i + 1) % length
        j = (j + 1) % length

    return new_order


if __name__ == '__main__':
    parent_1 = [2, 1, 6, 4, 0, 8, 3, 7, 9, 5]
    parent_2 = [3, 9, 5, 6, 0, 7, 8, 4, 2, 1]
    first_cut, second_cut = 3, 7
    expected = [5, 6, 7, 4, 0, 8, 3, 2, 1, 9]
    actual = _order_crossover_calculator(parent_1, parent_2, first_cut, second_cut)
    print(expected == actual)
