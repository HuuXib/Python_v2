import random 

text = input("Podaj tekst do zaszyfrowania: ")
count_char = len(text)
ascii_values = [ord(char) for char in text]

with open ('key.txt', 'w', encoding='utf-8') as file:
    pass
    

for i in range(count_char):
    x = random.randint(97,122)
    with open('key.txt', 'a', encoding='utf-8') as file:
        file.write(f"{str(x)} ")
    add_value = (ascii_values[i] + x)%ascii_values[i]
    ascii_values[i] = ascii_values[i] + add_value
text = ''.join(chr(value) for value in ascii_values)
print(text)