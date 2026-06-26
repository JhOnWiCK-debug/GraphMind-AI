import subprocess

with open(
    "evaluation_questions.txt",
    "r",
    encoding="utf-8"
) as f:

    questions = [
        line.strip()
        for line in f
        if line.strip()
    ]

print(
    f"Loaded {len(questions)} questions"
)

for i, question in enumerate(
    questions,
    start=1
):

    print("\n" + "=" * 60)

    print(
        f"Question {i}: {question}"
    )

    result = subprocess.run(
        [
            "python",
            "app/agentic_rag/final_graphrag.py"
        ],
        input=question,
        text=True,
        capture_output=True
    )

    print(
        result.stdout
    )