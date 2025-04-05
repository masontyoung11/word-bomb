import os


file_location = '../original-words.txt'
output_files = {
    'beginner': '../beginner-words.txt',
    'intermediate': '../intermediate-words.txt',
    'advanced': '../advanced-words.txt'
}
category_counts = {'beginner': 0, 'intermediate': 0, 'advanced': 0}


def categorize_word(word: str) -> str:
    if len(word) <= 5:
        if '_' in word:
            return 'advanced'
        return 'beginner'
    elif 6 <= len(word) <= 10:
        if '_' in word:
            return 'advanced'
        return 'intermediate'
    else:
        return 'advanced'


if os.path.exists(file_location):
    with open(file_location) as diary_file:
        for line in diary_file:
            category = categorize_word(line.strip().lower())
            
            print(f"Categorizing {line.strip()} as {category}...")
            category_counts[category] += 1
            
            
            with open(output_files[category], "a") as output_file:
                output_file.write(line)
    
    print("\nCategory counts:")
    for category, count in category_counts.items():
        print(f"{category.capitalize()}: {count}")
else:
    print(f"Error: The file at '{file_location}' does not exist.")