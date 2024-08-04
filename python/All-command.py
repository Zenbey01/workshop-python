# การแสดงผล ใช้คำสั่ง print
print("Hello PyThon : การแสดงผล ใช้คำสั่ง print")

# การคอมเม้นท์ จะใช้สัญลักษณ์ #
print("การแสดงคอมเม้นท์ : แบบบรรทัดเดียว") # การแสดงคอมเม้นแบบไว้ด้านข้าง
''' การแสดงคอมเม้นแบบใช้ ' ' ' ข้อความ ' ' '
print("การแสดงคอมเม้นท์ : แบบหลายบรรทัด 1")
print("การแสดงคอมเม้นท์ : แบบหลายบรรทัด 2")
print("การแสดงคอมเม้นท์ : แบบหลายบรรทัด 3")
'''
""" การแสดงคอมเม้นแบบใช้ " " " ข้อความ " " "
print("การแสดงคอมเม้นท์ : แบบหลายบรรทัด 1")
print("การแสดงคอมเม้นท์ : แบบหลายบรรทัด 2")
print("การแสดงคอมเม้นท์ : แบบหลายบรรทัด 3")
"""

# การใช้ฟังก์ชัน print
# string => ข้อความ ตัวอักษร จะใช้ภายใต้เครื่องหมาย ',''',""
print('การใช้ฟังก์ชัน print (string) : ด้วยเครื่องหมาย single quote')
print("การใช้ฟังก์ชัน print (string) : ด้วยเครื่องหมาย double quote")
# number => integer, float
print(3.99)
# boolean => true, false
print(True)
# ขึ้นบรรทัดใหม่ด้วย \n
print("Hello\nworld")
# การเว้นวรรคแบบ tap ด้วย \t
print("Hello\tworld")
# การเขื่อมประโยคด้วยเครื่องหมาย + ("string")
print("Hello " + "world")
# หากเป็นตัวเลข จะเป็นการบวกเลขกัน
print(5+5)

# ชนิดข้อมูลพื้นฐาน
# string : str เป็นข้อมูลชนิดตัวอักษร
print("ข้อมูลชนิดตัวอักษร : This is an apple 2044")
# integer : int เป็นข้อมูลตัวเลข ชนิดจำนวนเต็มบวก/จำนวนเต็มลบ
print(-11,0,11)
# floating point : float คือข้อมูลตัวเลข ขนิดทศนิยม
print(-14.2,2.0,3.6)
# booleans : bool คือข้อมูล logical ที่มีแค่ true และ false
print(True)

# ชนิดข้อมูลขั้นสูง
# lists : list คือชนิดข้อมูลที่อยู่ในรูปแบบ object และสามารถเปลี่ยนแปลงข้อมูลภายในได้
print([10,12.5,"list"])
# dictionaries : dict คือข้อมูลที่จับคู่ระหว่าง key:value โดย key จะเป็น index เข้าถึงข้อมูลและ value จะเป็นค่าของข้อมูลที่สอดคล้องกัน
print({1: 'One', 2: 'Two', 3: 'Three'})
# tuples : tup คือข้อมูลที่ทำหน้าที่คล้าย list แต่มีความแตกต่างที่ tuples เก็บได้เพียงข้อมูลที่ไม่สามารถเปลี่ยนแปลงได้เท่านั้น
print(10.1,"ten",-12)
# sets : set คือ object ที่ใช้สำหรับการเก็บข้อมูลที่ไม่ซ้ำกัน
print("a","b")

# โครงสร้าง Variable
# ชื่อตัวแปร = ค่าที่เก็บในตัวแปร <-- ทั่วไป
x = 109
y = 18.8
print("ผลลัพธ์ของค่า variable = " +str(x)) # การแปลงข้อมูล int เป็น string โดยใช้คำสั่ง str()
print(x,y)
print(type(y)) #การเช็คชนิดข้อมูล ใช้คำสั่ง type
print(type("ชนิดข้อมูล : string")) #การเช็คชนิดข้อมูล ใช้คำสั่ง type

""" กฎการตั้งชื่อ
# 1. สามารถใส่ตัวเลข ตัวอักษร เครื่องหมายได้
# 2. ห้ามขึ้นต้นด้วยตัวเลขและสัญลักษณ์ ยกเว้น _ หน้าชื่อ
# 3. ห้ามซ้ำกับ keyword หรือคำสงวน
# 4. case sensitive
"""

a = 10
a1 = 15
_a1 = "แบบ _ อยู่ด้านหน้า"

name = "A"
NAME = "B"
naME = "C"

print(name)
print(NAME)
print(naME)

# การแปลงชนิดข้อมูล type coversion สามารถทำได้จากการเอาชนิดข้อมูลไปครอบข้อมูลที่ต้องการ เช่น str(a) int(b)
q = 10
w = 10.3
e = "14"
r = 5
# การแปลงแบบถาวร
r = str(r)
print(type(q))
print(type(r))
# การแปลง
# str => int
result1 = q-int(e)
# int => str
result2 = str(q)+e
print(result1)
print(result2)
print(type(result1))
print(type(result2))

# function input
Name = input("การเขียนข้อความในฟังก์ชัน input => เขียนชื่อของนายสิ :\t") #รับค่ามาแล้วเก็บลงในตัวแปร Name
print("ดูสิ่งที่พิมพ์มา = " + Name)
print(type(Name))

fname = input("input name :")
lname = input("input last name :")
print("your name is " +fname)
print("your name is " +lname)

a = input("Number 1 : ")
b = input("Number 2 : ")
# process
c = int(a)+int(b)
print(c)