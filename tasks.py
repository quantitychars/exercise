
diapason = []
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
class Diapason:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def difference(self):
        return self.right - self.left

    def print_numbers(self):
        diapason_for_binary = []
        for number in range(self.left, self.right + 1):
            diapason_for_binary.append(number)
        return diapason_for_binary


input_left = int(input("Please enter a number left: "))
input_right = int(input("Please enter a number right: "))

diapason.append(Diapason(input_left, input_right))

count_prime_set_bits = 0

for d in diapason:
    numbers = d.print_numbers()

    for number in numbers:
        set_bits = number.bit_count()


        if is_prime(set_bits):
            count_prime_set_bits += 1

print("Answer:", count_prime_set_bits)







