def rating(total: int, word: str):
    dict_rating = dict(zip(["terrible", "poor", "good", "great", "excellent"], [0, 0.5, 0.10, 0.15, 0.20]))
    if word.lower() in dict_rating:
        return f"{word.capitalize()}: {total * dict_rating[word]}"
    else:
        return "Rating not recognised"
    
print(rating(50, "great"))
