#dummy text
text = """ Nepal is a beautiful country. Nepal has Mount Everest. Everest is the highest mountain in the world. Many tourists visit Nepal every year to see Everest and other mountains. Nepal is known for its mountains and natural beauty. """

def word_frequency(text):
  text = text.lower()

  for ch in [",", ".", "!", "?"]:
    text = text.replace(ch, "")

  #splitting the entire paragraph into seperate words
  words = text.split()

  frequency = {}
  for word in words:
    if word in frequency:
      #if the word already exists, then increase its counter by 1
      frequency[word] += 1
    else:
      #if the word doesn't already exist, then set the value to 1
      frequency[word] = 1

  #sorting the values from higesht to lowest
  sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

  frequent = sorted_words[:3]

  #displaying the top 3 words
  print("Top 3 words:")
  for word, count in frequent:
      print(f"{word} — {count} times")

word_frequency(text)
