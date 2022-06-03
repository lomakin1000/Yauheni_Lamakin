




n = int(input("Please enter the number of lines "))  
m = int(input('Please enter the number of columns '))
l = int(input('Please enter the quantity - between + '))
h = int(input('Please enter the quantity | between + '))


a = "+"  
b = "-" * l   # переменная с минусами между плюсами 
c = (("|" + (" " * l)) * m + "|\n")   # линия с вертикальной чертой
line_2 = c * h # линия с вертикальной чертой умноженная на кол. | между +

line_1 = (a + b) * m + a + "\n"  # переменная с линией +--+

str_1 = (line_1 + line_2) * n + line_1

print(str_1)








