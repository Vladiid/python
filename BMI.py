# Body mass index

m = float(input("Введите ваш вес в кг: "))
h = float(input("Введите ваш рост в см: "))
h = h/100
index_mass = round((m / (h*h)),2)

if index_mass < 16:
    print ("Индекс массы тела равен:", index_mass, "кг/м², у Вас выраженный дефицит массы тела.")
elif 16 <= index_mass <= 18.5:
    print ("Индекс массы тела равен:", index_mass, "кг/м², у Вас недостаточная (дефицит) масса тела.")
elif 18.5 <= index_mass <= 24.99:
    print ("Индекс массы тела равен:", index_mass, "кг/м², у Вас норма!")
elif 25 <= index_mass <= 30:
    print ("Индекс массы тела равен:", index_mass, "кг/м², у Вас избыточная масса тела (предожирение).")
elif 30 <= index_mass <= 35:
    print ("Индекс массы тела равен:", index_mass, "кг/м², у Вас ожирение первой степени.")
elif 35 <= index_mass <= 40:
    print ("Индекс массы тела равен:", index_mass, "кг/м², у Вас ожирение второй степени.")
elif index_mass >= 40:
    print ("Индекс массы тела равен:", index_mass, "кг/м², у Вас ожирение третьей степени (морбидное)!")

