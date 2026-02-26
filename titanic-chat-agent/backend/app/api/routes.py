from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.agent.agent_builder import generate_code
from app.services.executor import execute_code

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    code = generate_code(request.message)

    execution_result = execute_code(code)

    return ChatResponse(
        answer=execution_result["answer"],
        image=execution_result["image"]
    )