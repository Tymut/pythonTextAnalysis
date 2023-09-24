import string

with open("plainText.txt", "r", encoding="utf-8") as f:
    text = f.read()

aliases = {
    " ": "Spacja",
    "\t": "Tabulator",
    "\n": "Nowa linia",
    "\r": "Carriage Return",
    "\x0b": "x0b",
    "\x0c": "x0c"
}


def count(txt, char):
    counter = 0
    for z in txt:
        if z == char:
            counter += 1
    return counter


# Konwersja do .lower() eliminuje konieczność rozróżniania dużych liter od małych
# print(count(text, "a") + count(text, "A"))
# print(count(text.lower(), "a"))
# print(count(text.lower(), "z"))

sum_of_percent = list()

for index in string.printable:
    how_many = count(text, index)
    percent = 100 * how_many / len(text)
    sum_of_percent.append(percent)
    if index in aliases.keys():
        print("{0} - {1} - {2}%".format(aliases[index], how_many, round(percent, 2)))
    else:
        print("{0} - {1} - {2}%".format(index, how_many, round(percent, 2)))
print("{0} - {1}%".format("Łącznie", round(sum(sum_of_percent), 2)))
