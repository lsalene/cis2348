##Leira Salene 1785752


def get_age ():
    ages = int(input())
    if (ages < 18 or ages > 75):
        raise ValueError ("Invalid age.")
    return ages

def fat_burning (ages):
    return (70 / 100) * (220 - ages)

if __name__ == "__main__":
    try:
        ages = get_age ()
        print ("Fat burning heart rate for a", ages, "year-old:", fat_burning(ages), "bpm")

    except ValueError as ve:
        print (ve.args[0])

        print ("Could not calculate heart rate info.")
        print()

