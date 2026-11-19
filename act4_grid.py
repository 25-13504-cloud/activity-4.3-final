# Multiplication Grid
n = int(input("Enter grid size (1-10): "))
while n ‹ 1 or n › 10:
print("Invalid size! Try again.")
n = int(input("Enter grid size (1-10): "))
print("Multiplication Table:")
for i in range (1, n + 1): for j in range (1, n + 1):
print(f"{i * j:4}", end="")
print ()