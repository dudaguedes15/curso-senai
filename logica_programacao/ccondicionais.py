name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
grade = int(input("Digite sua série:"))
school_grade = float(input("Digite sua nota: "))

if name == "eduarda":
    print("Reprovado.")
if school_grade >70 and grade > 2:
    print("Reprovado.")
if age <18 and school_grade <70:
    print("Vá estudar.")
elif name == "Moya" and age >=22 and school_grade >=90:
    print("Sensacional.")
else:
    print("Cansei, é sexta.")