white_space = "lots of space at the end           "
print(len(white_space))
print(len(white_space.strip()))


example_text = "here's some text with lots of text"
print(example_text.count("text"))  #counts number of text in string
print(example_text.count("t"))


print(example_text.lower()) #makes all lower case
print(example_text.upper()) #makes all upper case
print(example_text.title()) #makes the start of each word capital
print(example_text.capitalize()) #capitalises the first letter

print(example_text.replace("with", "without")) #replaces parts of a string
