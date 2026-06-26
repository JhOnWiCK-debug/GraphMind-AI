from critic import evaluate_answer

question = "What is Vishva's CGPA?"

context = """
Vishva's CGPA is 8.57.
"""

answer = """
Vishva's CGPA is 7.5.
"""

result = evaluate_answer(
    question,
    context,
    answer
)

print(result)