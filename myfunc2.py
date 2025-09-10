# myfunc2.py

def subtract_numbers(a, b):
    """
    ฟังก์ชันการดำเนินการลบเลข 2 ชุด
    รับค่า a และ b แล้วคืนค่า a - b
    """
    return a - b


if __name__ == "__main__":
    # ตัวอย่างการทดสอบฟังก์ชัน
    x = 15
    y = 7
    print(f"{x} - {y} = {subtract_numbers(x, y)}")
