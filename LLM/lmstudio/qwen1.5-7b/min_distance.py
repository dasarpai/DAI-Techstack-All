import sys

def min_distance(s):
    if not s:
        return None

    char_positions = {}
    min_dist = float('inf')
    min_char = None

    for i, char in enumerate(s):
        if char in char_positions:
            dist = i - char_positions[char]
            if dist < min_dist:
                min_dist = dist
                min_char = char
        else:
            char_positions[char] = i

    if min_dist == float('inf'):
        return None
    else:
        # Find the first occurrence of the minimum-distance repeating character
        for i, char in enumerate(s):
            if char == min_char and (char_positions[min_char] - i) == min_dist:
                return (min_dist, min_char)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <string>")
    else:
        result = min_distance(sys.argv[1])
        print(result)

if __name__ == "__main__":
    main()
