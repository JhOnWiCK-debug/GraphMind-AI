from persistent_memory import (
    PersistentMemory
)

memory = PersistentMemory()

memory.add(
    "Where does Wheelz import from?",
    "China"
)

memory.add(
    "What currency do they use?",
    "Yuan"
)

print()

for row in memory.history():

    print(row)