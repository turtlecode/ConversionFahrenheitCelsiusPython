def convert(s):
    f = float(s)
    c = (f-32)* 5/9
    print("Celsius value of the entered value :", c)


fahrenheit = int(input("Enter the Fahrenheit value? :"))
convert(fahrenheit)