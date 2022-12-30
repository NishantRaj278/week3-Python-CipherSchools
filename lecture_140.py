# dictionary comprehension

square={num:num**2 for num in range(1,11)}
print(square)

square={f"Square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")
string="Muskan"    
word_count={char:string.count(char) for char in string}
print(word_count)
