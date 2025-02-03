import aiohttp
import math

class FunFacts:
    def __init__(self, session):
        self.url = 'http://numbersapi.com/'
        self.session = session  # Use a single session

    async def get_fact(self, number):
        try:
            async with self.session.get(f'{self.url}{number}/math?json') as response:
                response.raise_for_status()
                return await response.json()
        except Exception:
            return {"text": "Fact not available"}

    def check_parity(self, number):
        return 'even' if number % 2 == 0 else 'odd'

    def check_prime(self, number):
        if number < 2:
            return False
        if number in (2, 3):
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(abs(number))) + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False
        return True

    def check_armstrong(self, number):
        num_str = str(abs(number))
        power = len(num_str)
        return sum(int(digit) ** power for digit in num_str) == abs(number)

    def digit_sum(self, number):
        return sum(int(digit) for digit in str(abs(number)))

    def check_perfect(self, number):
        return sum(i for i in range(1, abs(number) // 2 + 1) if abs(number) % i == 0) == abs(number)