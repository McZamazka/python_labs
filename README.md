**Прграммирование и алгоритмизация (Лабараторные)**

**Лабараторная №2:**

**Задание №1:**
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print("Првиет, " + name + "!", "Через год тебе будет " + str(age+1) + ".")
```

![exe1](/images/lab01/exe01.png)
----------------------------------------------------
**Задание №2:**
```python
a = input()
b = float(input())
print("a: " + a.replace('.', ','))
print("b: " + str(b))
print("sum=" + f"{(float(a)+b):.2f}" + ";" + " avg=" + f"{(float(a)+b)/2:.2f}")
```

![exe1_1_1!][/images/lab02/exe1_1_1.png]
![exe1_1_2!][/images/lab02/exe1_1_2.png]
----------------------------------------------------
**Задание №3:**
```python
price = int(input())
discount = int(input())
vat = int(input())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print("База после скидки: " + f"{base:.2f}" + " ₽")
print("НДС: " + f"{vat_amount:.2f}" + " ₽")
print("Итого к оплате: " + f"{total:.2f}" + " ₽")
```

![exe1_1_1!][/images/lab02/exe1_1_1.png]
![exe1_1_2!][/images/lab02/exe1_1_2.png]
----------------------------------------------------
**Задание №4:**
```python
m = int(input("Минуты: "))
print(str(m//60) + ":" + f"{(m%60):02d}")
```

![exe1_1_1!][/images/lab02/exe1_1_1.png]
![exe1_1_2!][/images/lab02/exe1_1_2.png]
----------------------------------------------------
**Задание №5:**
```python
a, b, c = map(str, input().split())
print("ФИО: ", a, b, c)
print("Инициалы: ", a[0] + b[0] + c[0] + '.')
print("Длина (символов): " + str(len(a) + len(b) + len(c) + 2))
```

![exe1_1_1!][/images/lab02/exe1_1_1.png]
![exe1_1_2!][/images/lab02/exe1_1_2.png]
----------------------------------------------------
