import asyncio
from typing import List
import time

async def sleep_sort(arr: List[float], base_delay: float = 0.042) -> List[float]:
    """
    Sort an array by using sleep timers for each element.
    
    Args:
        arr: List of numbers to sort
        base_delay: Base delay multiplier in seconds (default: 0.1)
        
    Returns:
        Sorted list of numbers
    
    Raises:
        ValueError: If input is not a list or contains non-numeric values
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if not arr:
        return []
    
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numbers")
    
    result = []
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val if max_val != min_val else 1
    
    async def add_number(num: float):
        # Normalize the delay to prevent extremely long waits
        normalized_delay = ((num - min_val) / range_val) * base_delay
        await asyncio.sleep(normalized_delay)
        result.append(num)
    
    # Create tasks for all numbers
    tasks = [add_number(num) for num in arr]
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    
    return result

async def main():
    # Example usage
    test_arrays = [
        [42,5, 2, 8, 1, 9, 3, 7, 4, 6],
        [10.42, 3.2, 7.8, 2.1],
        [1],
        []
    ]
    
    for arr in test_arrays:
        print(f"\nSorting array: {arr}")
        start_time = time.time()
        
        try:
            sorted_arr = await sleep_sort(arr)
            elapsed = time.time() - start_time
            print(f"Sorted array: {sorted_arr}")
            print(f"Time taken: {elapsed:.3f} seconds")
            
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())