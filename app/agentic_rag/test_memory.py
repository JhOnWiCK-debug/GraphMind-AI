from conversation_memory import (
    ConversationMemory
)

memory = ConversationMemory()

memory.add(
    "Where does Wheelz import from?",
    "China"
)

memory.add(
    "What currency is used there?",
    "Yuan"
)

for item in memory.get_history():

    print(item)