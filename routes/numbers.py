from api.numbers_api import FunFacts

from fastapi import APIRouter, HTTPException

router = APIRouter()
facts = FunFacts()

@router.get("/{number}")
async def get_number_fact(number: int):
    try:
        fun_fact = await facts.get_fact(number)
    except Exception as e:
        return {"number": number, "error": True}
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative")
    properties = []
    is_armstrong = facts.check_armstrong(number)
    if is_armstrong:
        properties.append("armstrong")
    is_even = facts.check_parity(number)
    properties.append(is_even)
    is_prime = facts.check_prime(number)
    digit_sum = facts.digit_sum(number)
    is_perfect = facts.check_perfect(number)
    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fact": fun_fact['text'],
    }