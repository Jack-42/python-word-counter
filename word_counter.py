import re

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin eu erat eget turpis sagittis bibendum sed vestibulum nibh. Curabitur sed aliquet mauris. Praesent sapien orci, cursus ut tristique vel, cursus et mi. Sed nec mauris vulputate, feugiat ligula ut, sollicitudin nisi. Nunc finibus, erat et suscipit tincidunt, orci nisl pulvinar nibh, id dapibus est velit eget risus. Nam elementum sollicitudin tincidunt. Duis aliquam convallis neque, ut sollicitudin erat congue eu. Aliquam posuere congue leo, eget fermentum nunc dignissim vel. Nam at aliquet eros.
Maecenas at justo quam. Integer pharetra leo sed ante pellentesque accumsan sit amet sed lacus. Donec accumsan felis vel lacus finibus, sit amet dapibus neque hendrerit. Nam sollicitudin leo enim, vel semper tortor ultrices eu. Morbi elementum nulla ex, et viverra massa rutrum ornare. Curabitur euismod dolor sit amet est faucibus, vel euismod mi rutrum. Etiam augue odio, porttitor id pulvinar et, finibus id nibh. Donec mi neque, mollis quis iaculis quis, aliquam non lacus. Nunc vehicula velit eu sodales pellentesque. Fusce sit amet eleifend risus, sit amet sollicitudin turpis. Nam consequat in orci quis hendrerit. Integer quis est ac libero viverra feugiat vel sed mauris. Phasellus vel volutpat mi. Quisque ac elit lacus. Phasellus tristique nibh in mollis viverra.
Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin et erat nisi. Nulla nec velit vel erat tristique dignissim. Duis dignissim laoreet erat, sed mollis ex ornare et. In et consequat eros. Nulla in dolor ultricies, lacinia purus quis, aliquam purus. Nunc mi turpis, condimentum vel enim at, scelerisque eleifend erat. Donec vehicula dictum neque semper pretium. Sed id arcu vel ligula accumsan imperdiet nec vitae mi. Integer non augue porttitor, viverra turpis et, ultricies diam. In lacus ligula, viverra sed tellus id, cursus maximus sapien. Curabitur justo purus, bibendum nec dui et, laoreet efficitur leo."""


def main():
    filtered_text = filter_text(lorem_ipsum)
    words = tokenize(filtered_text)
    word_counts = count_words(words)
    for word in word_counts:
        print(word + ": " + str(word_counts[word]))


def filter_text(text):
    filtered_text = text
    invalid_chars = ",;.:-_^!\"§$%&/()=?{[]}\\#\'+*~"
    for char in invalid_chars:
        filtered_text = filtered_text.replace(char, "")
    return filtered_text


def tokenize(text):
    words = []
    lines = text.splitlines()
    for line in lines:
        curr_words = line.split()
        words.extend(curr_words)
    return words


def count_words(words):
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts


if __name__ == "__main__":
    main()
