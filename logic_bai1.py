import re

# Kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression):
    # Kiểm tra các ký tự hợp lệ
    valid_chars = re.compile(r'^[A-Z∧∨¬→() ]+$')
    if not valid_chars.match(expression):
        return False
    
    # Kiểm tra cặp dấu ngoặc
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    
    return True

# Đánh giá biểu thức logic
def evaluate_expression(expression, values):
    # Thay thế các biến bằng giá trị của chúng
    for var, val in values.items():
        expression = expression.replace(var, str(val))
    
    # Thay thế các toán tử logic
    expression = expression.replace('∧', ' and ')
    expression = expression.replace('∨', ' or ')
    expression = expression.replace('¬', ' not ')
    expression = expression.replace('→', ' <= ')
    
    # Đánh giá biểu thức
    try:
        result = eval(expression)
    except:
        return None
    
    return result

# Nhập biểu thức logic từ bàn phím
expression = input("Nhập biểu thức logic (ví dụ: (A ∧ B) → ¬C): ")

# Kiểm tra tính hợp lệ của biểu thức
if is_valid_expression(expression):
    print("Biểu thức hợp lệ.")
    
    # Nhập giá trị cho các biến từ bàn phím
    values = {}
    variables = re.findall(r'[A-Z]', expression)
    for var in set(variables):
        val = input(f"Nhập giá trị cho {var} (True/False): ")
        values[var] = True if val.lower() == 'true' else False
    
    # Đánh giá biểu thức với các giá trị đầu vào
    result = evaluate_expression(expression, values)
    if result is not None:
        print(f"Kết quả của biểu thức với các giá trị đầu vào: {result}")
    else:
        print("Có lỗi khi đánh giá biểu thức.")
else:
    print("Biểu thức không hợp lệ.")
