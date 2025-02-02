import asyncio
from fastapi import APIRouter, HTTPException, Request, Query
from api.numbers_api import FunFacts

router = APIRouter()

@router.get("/api/classify-number")
async def get_number_fact(request: Request, number: int = Query(..., description="The number to classify")):
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative")

    facts = request.app.state.facts


    fun_fact_task = facts.get_fact(number)

    # Execute the synchronous checks directly
    is_armstrong = facts.check_armstrong(number)
    is_even = facts.check_parity(number)
    is_prime = facts.check_prime(number)
    digit_sum = facts.digit_sum(number)
    is_perfect = facts.check_perfect(number)


    fun_fact = await fun_fact_task

    properties = [is_even]
    if is_armstrong:
        properties.append("armstrong")

    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact.get("text", "Fact not available"),
    }
