#!/usr/bin/env python3

def sum_list(input_list: list[float]) -> float:
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
