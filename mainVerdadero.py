def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

if __name__ == "__main__":
    print("División:", dividir(10, 2))
