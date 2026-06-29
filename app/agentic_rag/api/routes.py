from fastapi import APIRouter

from .models import (
    AskRequest,
    AskResponse
)

from .engine import (
    engine
)

from ..run_agent import (
    run_agent
)

router = APIRouter()


@router.post(
    "/ask",
    response_model=AskResponse
)
def ask_question(
    request: AskRequest
):

    answer = run_agent(
        request.question,
        engine.graph,
        engine.retriever,
        engine.documents
    )

    return AskResponse(
        answer=answer
    )