__author__ = 'Lemmeister'


# Exercise 10.1
def nested_sum(a_list):
    new_list = []
    for l in a_list:
        total = 0
        for i in l:
            total += i
        new_list.append(total)
    print('Exercise 10.1: %s' % new_list)

nested_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#nested_sum(nested_list)


# Exercise 10.2
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(a_list):
    new_nested_list = []
    for i in a_list:
        new_nested_list.append(capitalize_all(i))
    return new_nested_list


nested_list = [['l', 'e', 'm', 'u', 'e', 'l']]
#print('Exercise 10.2: %s' % capitalize_nested(nested_list))


# Exercise 10.3
def summation(a_list):
    sums = []
    total = 0
    for i in a_list:
        total += i
        sums.append(total)
    return sums

numbers = [1, 2, 3, 4, 5]
#print('Exercise 10.3: %s' % summation(numbers))


# Exercise 10.4
def middle(a_list):
    return a_list[1:-1]

numbers = [1, 2, 3, 4]
#print('Exercise 10.4: %s' % middle(numbers))


# Exercise 10.5
def chop(a_list):
    del a_list[0]
    del a_list[-1]
    print('Exercise 10.5: %s' % a_list)
    return None

numbers = [1, 2, 3, 4]
#chop(numbers)


# Exercise 10.6
def is_sorted(a_list):
    index = 0
    for i in a_list:
        if a_list[index] > a_list[index+1]:
            return False
        else:
            if index == len(a_list)-2:
                return True
            else:
                index += 1
    return True

my_list = [1, 2, 3, 4, -1]
#print('Exercise 10.6: %s' % is_sorted(my_list))


# Exercise 10.7
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = 'gwapoko'
str2 = 'kogwapo'
#print('Exercise 10.7: %s' % is_anagram(str1, str2))


# Exercise 10.8 Problem 1
def has_duplicates(a_list):
    for i in a_list:
        count = 0
        for l in a_list:
            if l == i:
                count += 1
                if count == 2:
                    return True
    return False

a_list = [1, 1, 2, 3, 4, 5]
#print('Exercise 10.8 Problem 1: %s' % has_duplicates(a_list))


# Exercise 10.8 Problem 2
import random

NUMBER_OF_STUDENTS = 23
TRIALS = 100


def generate_random_birthdays():
    return [random.randint(1, 365) for student in range(NUMBER_OF_STUDENTS)]


def stats(TRIALS):
    duplicate_count = 0
    for i in range(TRIALS):
        if has_duplicates(generate_random_birthdays()):
            duplicate_count += 1
    print('Exercise 10.8 Problem 2: ' + "In %d classrooms with %d students, %.1f%% had students\
 with duplicate birthdays." % (TRIALS, NUMBER_OF_STUDENTS, (float(duplicate_count) / TRIALS) * 100))

#stats(TRIALS)


# Exercise 10.9
def remove_duplicates(a_list):
    return list(set(a_list))

a_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
#print('Exercise 10.9: %s' % remove_duplicates(a_list))


# Exercise 10.10 Version 1
with open('words.txt') as fd:
    words = fd.read().split()


def read_words_v1(words):
    word_list = []
    for line in words:
        line = line.strip()
        word_list.append(line)
    return word_list

#print('Exercise 10.10 Version 1: %s' % type(read_words_v1(words)))


# Exercise 10.10 Version 2
def read_words_v2(words):
    word_list = []
    for line in words:
        line = line.strip()
        word_list += [line]
    return word_list

#print('Exercise 10.10 Version2: %s' % type(read_words_v2(words)))


# Exercise 10.11
with open('words.txt') as fd:
    word_list = fd.read().splitlines()


def bisect(myWord, myList):
    original = myList
    while True:
        middle = int(len(myList) / 2)
        if myWord > myList[middle]:
            myList = myList[middle:]
        elif myWord < myList[middle]:
            myList = myList[:middle]
        elif myWord == myList[middle]:
            return original.index(myWord)

        if len(myList) == 1:
            if myWord != myList[:]:
                return None
            else:
                return original.index(myWord)


#print('Exercise 10.11: %s' % bisect("danger", word_list))


# Exercise 10.12
with open('words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}

def find_rev_pairs(word_dict):
    for word in word_dict:
        if word[::-1] in word_dict:
            print(word, word[::-1])

#print('Exercise 10.12:')
#find_rev_pairs(word_dict)


# Exercise 10.13
with open('words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}


def split_word(word):
    word1 = word[::2]
    word2 = word[1::2]
    return word1, word2


def find_interlocked():
    for word in word_dict:
        split0 = split_word(word)[0]
        split1 = split_word(word)[1]
        if split0 in word_dict and split1 in word_dict:
                print(word, split0, split1)


def split_word2(word, i):
    split0 = word[i::3]
    split1 = word[i + 1::3]
    split2 = word[i + 2::3]
    return split0, split1, split2


def find_3way():
    answer = []
    for word in word_dict:
        for i in range(0, 3):
            split_ = split_word2(word, i)
            if (split_[0] in word_dict and
                split_[1] in word_dict and
                split_[2] in word_dict):
                    answer.append((word,
                           split_[0],
                           split_[1],
                           split_[2]))
    return answer

#print('Exercise 10.13: ')
#print(find_3way())


# Exercise 11.1
import uuid

with open('words.txt') as fd:
    words = fd.read().splitlines()

result = dict()


def dictionary():
    for line in words:
        result[line] = uuid.uuid4()
    return result

#print('Exercise 11.1:')
#print(dictionary())


# Exercise 11.2
def histogram(word):
    dictionary = dict()
    for character in word:
        dictionary[character] = 1 + dictionary.get(character, 0)
    return dictionary

#print('Exercise 11.2: %s' % histogram('lemuel jay vallinas'))


# Exercise 11.3
def print_hist(histogram):
    histoList = histogram.keys()
    for letter in sorted(histoList):
        print(letter, histogram[letter])

h = histogram('lemuel jay vallinas gwapo')
#print('Exercise 11.3:')
#print_hist(h)

# Exercise 11.4
def reverse_lookup(dictionary, value):
    results = []
    for key in dictionary:
        if dictionary[key] == value:
            results.append(key)
    return results


def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

h = histogram('lemuel jay vallinas')
k = reverse_lookup(h, 4)
#print('Exercise 11.4: %s' % k)


# Exercise 11.5
def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val, [])
        inv[val].append(key)
    return inv

hist = histogram('lemuel jay vallinas')
inv = invert_dict(hist)
#print('Exercise 11.5: %s' % inv)


# Exercise 11.6
known = {0: 0, 1: 1}


def fibonacci_given(n):
    if n in known:
        return known[n]
    else:
        res = fibonacci_given(n - 1) + fibonacci_given(n - 2)
    known[n] = res
    return res


def fibonacci_original(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_original(n - 1) + fibonacci_original(n - 2)


# Exercise 11.7
cache = {}


def ackermann(m, n):
    """
        Credits to the owner:
        http://thinkpython.com/code/ackermann_memo.py
    """
    """
    :param m:
    :param n:
    :return:
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

#print('Exercise 11.7:')
#print(ackermann(3, 4))
#print(ackermann(3, 6))


# Exercise 11.8 is very difficult. :3


# Exercise 11.9
def has_dups(myList):
    dictionary = {}
    for item in myList:
        dictionary[item] = 1 + dictionary.get(item, 0)
        if dictionary[item] > 1:
            return True
    return False

#listOne = [1, 2, 3, 4, 5, 5]
#print(has_dups(listOne))


# Exercise 11.10
def normalize(x):
    if x > 122:
        while x > 122:
            x -= 26
    elif x < 97:
        while x < 97:
            x += 26
    return x


def rotate_word(word, amount):
    new_word = ''
    for letter in word:
        letter = letter.lower()
        if ord(letter) + amount > 122:
            new_word += chr(normalize(ord(letter) + amount))
        elif ord(letter) + amount < 97:
            new_word += chr(normalize(ord(letter) + amount))
        else:
            new_word += chr(ord(letter) + amount)
    return new_word

with open('words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}


def find_rot_pairs():
    final_list = []
    for word in word_dict:
        for i in range(1, 26):
            if rotate_word(word, i) in word_dict:
                final_list.append((word, i, rotate_word(word, i)))
    final_list.sort()
    for pair in final_list:
        print(pair)

#print('Exercise 11.10:')
#find_rot_pairs()


# Exercise 11.11
def read_dictionary(filename):

    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def homophones(a, b, phonetic):
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]


def check_word(word, word_dict, phonetic):
    word1 = word[1:]
    if word1 not in word_dict:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True

phonetic = read_dictionary('words.txt')
word_dict = make_word_dict()
#print('Exercise 11.11:')
#for word in word_dict:
#    if check_word(word, word_dict, phonetic):
#        print(word, word[1:], word[0] + word[2:])


# Exercise 12.1
def sum_all(*args):
    return sum(args)

#print('Exercise 12.1:')
#print(sum_all(1, 2, 3))
#print(sum_all(1, 2, 3, 4, 5))
#print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Exercise 12.2
import random


def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def sort_by_length_random(words):
    t = []
    for word in words:
       t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res

words = ['Lemuel', 'Jay', 'Zoemar', 'Vince', 'George', 'Georges']

t = sort_by_length_random(words)
#print('Exercise 12.3.:')
#for x in t:
#    print(x)

# Exercise 12.3
text = 'The rain in Spain falls mainly on the plains!!!!'


def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)

#print('Exercise 12.3:')
#most_frequent(text)


# Exercise 12.4
# Exercise 12.5


# Exercise 12.6
def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        t = is_reducible(child, word_dict)
        if t:
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def children(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    if len(word) == 0:
        return
    print(word)
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for length, word in t[0:5]:
        print_trail(word)
        print('\n')

word_dict = make_word_dict()
#print('Exercise 12.6:')
#print_longest_words(word_dict)


# Exercise 13.1
from string import punctuation, whitespace

book = 'words.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed

#print("{} has {} 'words'".format(book, len([clean(word) for word in words])))

# Exercise 13.2
# Exercise 13.3
# Exercise 13.4
# Exercise 13.5
# Exercise 13.6
# Exercise 13.7
# Exercise 13.8
# Exercise 13.9

# Exercise 14.1
import os


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

#print('Exercise 14.1:')
#walk('.')
#walk2('.')


# Exercise 14.2
import sys


def sed(pattern, replace, source, dest):
    try:
        fin = open(source, 'r')
        fout = open(dest, 'w')

        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print('Something went wrong.')


def main(name):
    pattern = 'pattern'
    replace = 'replacendum'
    source = name
    dest = name + '.replaced'
    sed(pattern, replace, source, dest)

main(*sys.argv)


# Exercise 14.3
def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


#print('Exercise 14.3:')
#d = all_anagrams('words.txt')
#print_anagram_sets_in_order(d)
#eight_letters = filter_length(d, 8)
#print_anagram_sets_in_order(eight_letters)


# Exercise 14.4
import os


def walk(dirname):
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)


def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    for key, names in d.iteritems():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')


# Exercise 14.5



# Exercise 16.1



# Exercise 16.2


# Exercise 16.3
# Exercise 16.4

# Exercise 17.2
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print("x =", self.x, ",")
        print("y =", self.y)

#print('Exercise 17.2:')
#point = Point()
#point.print_point()
#point = Point(10)
#point.print_point()
#point = Point(20, 30)
#point.print_point()


# Exercise 17.3
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

#print('Exercise 17.3: ')
#point = Point()
#print(point)
#point = Point(10)
#print(point)
#point = Point(10, 15)
#print(point)


# Exercise 17.4
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

point1 = Point(1, 3)
point2 = Point(4, 5)
#print('Exercise 17.4:')
#print(point1 + point2)

# Exercise 17.5
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        point_ = Point()
        if isinstance(other, Point):
            point_.x += self.x + other.x
            point_.y += self.y + other.y
            return point_
        elif type(other) == tuple:
            point_.x += self.x + other[0]
            point_.y += self.y + other[1]
        return point_

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

point1 = Point(1, 6)
point2 = (5, 2)
point3 = point1 + point2
point4 = point2 + point1
#print('Exercise 17.6:')
#print(point3, point4)


# Exercise 18.1
class Time(object):
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def __lt__(self, other):
        return (self.hour, self.minute) < (other.hour, other.minute)

    def __gt__(self, other):
        return (self.hour, self.minute) > (other.hour, other.minute)

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __repr__(self):
        return '{}'.format((self.hour, self.minute))

a = Time(hour=3, minute=31)
b = Time(hour=4, minute=30)

#print('Exercise 18.1:')
#print(a < b)

