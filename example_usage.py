from client import GroverSearch

grover = GroverSearch(num_items=16, target_idx=7)
print("Initial target probability:", grover.get_target_probability())

grover.step()
print("Probability after 1 iteration:", grover.get_target_probability())

grover.step()
print("Probability after 2 iterations:", grover.get_target_probability())
