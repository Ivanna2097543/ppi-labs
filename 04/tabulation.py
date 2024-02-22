from matplotlib import pyplot as plt

def func(x: list[float], N: float, a: float) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [ N*(t/N + 0.5)**a - N/2 for t in x ]

def tabulate(a: float, b: float, n: int, N: float, a_val: float) -> tuple[list[float], list[float]]:
    x = [ a + x*(b - a)/n for x in range(n) ]
    y = func(x, N, a_val)
    return (x, y)

def main():
    res = tabulate(0, 1, 1000, 1, 2)

    plt.plot(res[0], res[1])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()