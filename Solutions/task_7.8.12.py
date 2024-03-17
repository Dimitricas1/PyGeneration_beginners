for bulls in range(1, 10):
    for cows in range(1, 18):
        for telyats in range(1, 171):
            if (
                bulls + cows + telyats == 100
                and bulls * 10 + cows * 5 + telyats * 0.5 == 100
            ):
                print(bulls, cows, telyats, sep=", ")
