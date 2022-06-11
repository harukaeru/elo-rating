def calculate_elo(left_rate, right_rate, is_left_win):
    if is_left_win:
        w_ab = 1 / (10 ** ((right_rate - left_rate) / 400) + 1)
        left_rate = left_rate + 32 * (1 - w_ab)
        right_rate = right_rate + 32 * (0 - w_ab)
    else:
        w_ba = 1 / (10 ** ((left_rate - right_rate) / 400) + 1)
        right_rate = right_rate + 32 * (1 - w_ba)
        left_rate = left_rate + 32 * (0 - w_ba)

    return left_rate, right_rate
