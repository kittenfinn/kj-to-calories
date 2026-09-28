
KJ_PER_KCAL = 4.184  # food "calories" are really kilocalories (kcal)

def kj_to_kcal(kj):
    return kj / KJ_PER_KCAL

if __name__ == "__main__":
    kj = float(input("Enter kilojoules (kJ): "))
    print(f"{kj} kJ = {kj_to_kcal(kj):.1f} Calories (kcal)")
