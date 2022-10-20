def compose(notes: list, moves: list[int], start: int) -> list:
    result = list()
    current = start
    result.append(notes[current % len(notes)])
    for move in moves:
        current = current + move
        result.append(notes[current % len(notes)])
    return result

result = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
print(result)