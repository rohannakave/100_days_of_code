import random
import Words
import Graph

print(Graph.logo)


def list_to_string(n):
    str1 = " "
    print(str1.join(n))


stages = Graph.stages
word_list = Words.word_list

lives = len(stages)

# word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
len_word = len(chosen_word)
vis_list = []

# For testing reference printed the solution.
print(f"Answer is:  {chosen_word}")

# To display _ instead of answer word.
for i in range(0, len_word):
    vis_list.append("_")

list_to_string(vis_list)

while "_" in vis_list:
    flag = 0  # To set the life of hangman. if Flag = 1 guessed letter exist in answer else user will lose 1 life.
    if lives > 0:
        guess = input("Guess a letter: ").lower()

        if guess in vis_list:
            print(f"You have already tried {guess} letter")
            continue

        for letter in range(0, len_word):
            if guess == chosen_word[letter]:
                vis_list[letter] = guess
                flag = 1

        if flag == 0:
            print(stages[lives - 1])
            lives -= 1
            print(f"You have entered {guess}, and it is not present in above word. You have {lives} lives remaining.")

        list_to_string(vis_list)
    else:
        break

if "_" not in vis_list:
    print("You Win!!")
else:
    print("You Lose!!")
