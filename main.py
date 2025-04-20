def calculate_pressure(force, area):
    if area == 0:
        return "المساحة لا يمكن أن تكون صفر!"
    pressure = force / area
    return pressure

if __name__ == "__main__":
    try:
        force = float(input("أدخل القوة (نيوتن): "))
        area = float(input("أدخل المساحة (متر مربع): "))
        result = calculate_pressure(force, area)
        print(f"الضغط = {result} باسكال")
    except ValueError:
        print("يرجى إدخال أرقام صحيحة!")