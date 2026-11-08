# =========== Please do not change the code here ===========
import pickle

with open('../data/papers.pkl', 'rb') as f:
    paper_data = pickle.load(f)

# =========== start your code here for Q3 ===========
# Please use `paper_data` created for you
# If you are not sure how to create `paper_data` using the starting code,
# please watch the video on Moodle under "Problem sets" -> "Hints and
# visualisation".

pair_counts = {}

# Iterate through all possible author pairs for a research paper, adding one to that author pair each time

for author in paper_data.values():
    for i in range(len(author)):
        for j in range(i + 1, len(author)):
            pair = tuple(sorted((author[i], author[j])))
            pair_counts[pair] = pair_counts.get(pair, 0) + 1

productive_pairs = {}

# Add all author pairs with >= 15 research papers to new tuple

for pair, count in pair_counts.items():
    if count >= 15:
        productive_pairs[pair] = count


# Check output

print(productive_pairs)