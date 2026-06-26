def plan_query(
    question
):

    question = question.lower()

    # SUMMARY

    if any(
        word in question
        for word in [
            "summarize",
            "summary",
            "overview",
            "what is the document about"
        ]
    ):
        return "SUMMARY"

    # HYBRID

    if (
        "currency" in question
        and "import" in question
    ):
        return "HYBRID"

    if any(
        phrase in question
        for phrase in [
            "tell me about",
            "information about",
            "details about"
        ]
    ):
        return "HYBRID"

    # FAISS

    if any(
        word in question
        for word in [
            "document",
            "pdf",
            "report",
            "assessment",
            "explain"
        ]
    ):
        return "FAISS"

    # GRAPH

    return "GRAPH"