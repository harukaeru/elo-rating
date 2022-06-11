def calculate_elo(left_rate, right_rate, is_left_win):
    w_ab = 1 / (10 ** ((right_rate - left_rate) / 400) + 1)
    if is_left_win:
        left_rate = left_rate + 32 * (1 - w_ab)
        right_rate = right_rate + 32 * (0 - w_ab)
    else:
        right_rate = right_rate + 32 * (1 - w_ab)
        left_rate = left_rate + 32 * (0 - w_ab)

    print('🐹', left_rate, right_rate)
    return left_rate, right_rate
