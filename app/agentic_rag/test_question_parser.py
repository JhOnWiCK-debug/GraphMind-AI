from question_parser import (
    parse_question
)

question = input(
    "Question: "
)

result = parse_question(
    question
)

print(
    result
)