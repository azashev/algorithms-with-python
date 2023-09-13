def find_all_solutions(idx, words_count, indexes_words, used_words, target):
    if idx >= len(target):
        print(' '.join(used_words))
        return
    if idx not in indexes_words:
        return
    for word in indexes_words[idx]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1

        find_all_solutions(idx + len(word), words_count, indexes_words, used_words, target)

        used_words.pop()
        words_count[word] += 1


words = input().split(', ')
target = input()

words_count = {}
indexes_words = {}


for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        index = 0
        while True:
            index = target.index(word, index)

            if index not in indexes_words:
                indexes_words[index] = []
            indexes_words[index].append(word)
            index += len(word)
    except ValueError:
        pass

find_all_solutions(0, words_count, indexes_words, [], target)

# Description
#
# Write a program that receives some strings and forms another string that is required.
#
# On the first line, you will be given all of the strings separated by comma and space.
# On the next line, you will be given the string that needs to be formed from the given strings.
# For more clarification see the examples below.
#
# Input:
# · On the first line, you will receive the strings (separated by comma and space ", ")
# · On the next line, you will receive the target string
#
# Output:
# · Print each of them found ways to form the required string as shown in the examples
#
# Constrains:
# · There might be repeating elements in the input
#
#
# Examples:
#
# Input:
# text, me, so, do, m, ran
# somerandomtex
#
#
# Expected output:
# so me ran do m text
#
#
#
# Input:
# Word, cruncher, cr, h, unch, c, r, un, ch, er
# Wordcruncher
#
#
# Expect output:
# Word cruncher
# Word cr unch er
# Word cr un c h er
# Word cr un ch er
# Word c r unch er
# Word c r un ch er
#
#
#
# Input:
# tu, stu, p, i, d, pi, pid, s, pi
# stupid
#
#
# Expected output:
# stu p i d
# stu pi d
# stu pid
# s tu p i d
# s tu pi d
# s tu pid
