import aiohttp
import math

class FunFacts:
    def __init__(self):
        self.url = 'http://numbersapi.com/'

    async def get_fact(self, number):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{self.url}{number}/math?json') as response:
                    response.raise_for_status()
                    return await response.json()
        except Exception as e:
            raise Exception(f"Error fetching fact: {e}")
    
    def check_parity(self, number):
        return 'even' if number % 2 == 0 else 'odd'
    
    def check_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    
    def check_armstrong(self, number):
        num_str = str(number)
        power = len(num_str)
        return sum(int(digit) ** power for digit in num_str) == number
    
    def digit_sum(self, number):
        return sum(int(digit) for digit in str(number))
    
    def check_perfect(self, number):
        return sum(i for i in range(1, number) if number % i == 0) == number