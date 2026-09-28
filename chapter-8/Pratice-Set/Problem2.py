def convert(a):
    return (a * (9/5)) + 32


a = int(input("Enter tempreture in celcius: "))

result = convert(a)
print(f"{round(result, 2)}°F")


