import re
import itertools

# Kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression):
    valid_chars = re.compile(r'^[A-Z∧∨¬→() ]+$')
    if not valid_chars.match(expression):
        return False
    
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
    for var, val in values.items():
        expression = expression.replace(var, str(val))
    
    expression = expression.replace('∧', ' and ')
    expression = expression.replace('∨', ' or ')
    expression = expression.replace('¬', ' not ')
    expression = expression.replace('→', ' <= ')
    
    try:
        result = eval(expression)
    except:
        return None
    
    return result

# Tìm tập giá trị cho các biến logic sao cho biểu thức mệnh đề là đúng
def find_values_for_expression(expression):
    if not is_valid_expression(expression):
        return "Biểu thức không hợp lệ."
    
    variables = sorted(set(re.findall(r'[A-Z]', expression)))
    for values in itertools.product([True, False], repeat=len(variables)):
        assignment = dict(zip(variables, values))
        if evaluate_expression(expression, assignment):
            return assignment
    
    return "Không có mẫu giá trị nào làm cho biểu thức đúng."

# Nhập biểu thức logic từ bàn phím
expression = input("Nhập biểu thức logic (ví dụ: (A ∨ B) ∧ (¬A ∨ C)): ")

# Tìm và in kết quả
result = find_values_for_expression(expression)
print(result)
