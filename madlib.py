with open("story.txt", "r") as f:
    story = f.read()

should_replace = set()
target_start = "["
target_end = "]"
target_word = -1

for i, char in enumerate(story):
    if char == target_start:
        target_word = i

    if char == target_end and target_word != -1:
        word = story[target_word : i + 1]
        should_replace.add(word)
        target_word = -1

answer = {}

for word in should_replace:
    new_input = input("Please add a " + word + ": ")
    answer[word] = new_input
    story = story.replace(word, answer[word])

print(story)
