def recommend_treadmill(income, fitness, usage):
    if income > 80000 and fitness >= 4:
        return "KP781 (Advanced)"
    elif income > 50000:
        return "KP481 (Mid-Level)"
    else:
        return "KP281 (Entry-Level)"
