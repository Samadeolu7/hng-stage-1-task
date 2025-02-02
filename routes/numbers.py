import asyncio
from fastapi import APIRouter, HTTPException, Request, Query
from api.numbers_api import FunFacts

router = APIRouter()

@router.get("/api/classify-number")
async def get_number_fact(request: Request, number: str = Query(..., description="The number to classify")):
    try:
        number = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Number must be an integer.")

    facts = request.app.state.facts  # Reuse the initialized FunFacts instance

    # Run tasks concurrently
    fun_fact_task = facts.get_fact(number)
    checks_task = asyncio.to_thread(
        lambda: (
            facts.check_armstrong(number),
            facts.check_parity(number),
            facts.check_prime(number),
            facts.digit_sum(number),
            facts.check_perfect(number),
        )
    )

    fun_fact, (is_armstrong, is_even, is_prime, digit_sum, is_perfect) = await asyncio.gather(fun_fact_task, checks_task)

    properties = []
    if is_armstrong:
        properties.append("armstrong")
    properties.append(is_even)

    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact.get("text", "Fact not available"),
    }