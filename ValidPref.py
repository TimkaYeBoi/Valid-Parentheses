class Solution(object):
    def isValid(self, s):
        # Словарь для хранения соответствий открывающих и закрывающих скобок
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # Если текущий символ является закрывающей скобкой
            if char in bracket_map:
                # Если стек пуст или верхний элемент стека не соответствует открывающей скобке
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                # Удаление последней открывающей скобки из стека
                stack.pop()
            else:
                # Добавление открывающей скобки в стек
                stack.append(char)

        # Валидность последовательности определяется пустотой стека
        return not stack

solution = Solution()
print(solution.isValid(s = "()[]{}"))  # Выведет True
print(solution.isValid(s = "([)]"))    # Выведет False
