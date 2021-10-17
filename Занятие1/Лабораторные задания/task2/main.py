if __name__ == "__main__":
    n = float(input("Введите размер оклада: "))  # Write your solution here
    print("Размер подоходного налога: ", n * 0.13)
    print("З/П на руки: ", n - n * 0.13)
