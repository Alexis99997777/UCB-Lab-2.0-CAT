"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########

    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
def choose(paragraphs, select, k):
    def helper(index,count):
        if index >= len(paragraphs):
            return ""
        if select(paragraphs[index]):
            if count == k:
                return paragraphs[index]
            else:
                return helper(index+1 , count+1)
        else:
            return helper(index+1 , count)
    return helper(0,0)

    "*** YOUR CODE HERE ***"
    # END PROBLEM 1

#about 是个函数 后期要传变量给他 所以要重新定义一个函数
def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def select(paragraphs):
        remove_punc = remove_punctuation(paragraphs)
        lower_punc = lower(remove_punc)
        words = split(lower_punc)
        for word in                                                                                                                                                                                                                                             :
            if word in topic:
                return True
        #把false放在外面可以保证每个变量都被检查到
        return False
    return select
    # END PROBLEM 2



    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.') # >= 
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.') # >= 
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.') #>=
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.') # >=
    50.0
    >>> accuracy('Cute', 'Cute Dog.') # < 
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
def accuracy(typed, reference):
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    matches = 0
    min_length = min(len(typed_words), len(reference_words))
    if not reference_words:
        if not typed_words:
            return 100.0
        else:
            return 0.0
    if not typed_words:
        return 0.0
    for index in range(min_length):
        if typed_words[index] == reference_words[index]:
            matches += 1
    return (matches / len(typed_words)) *100

    # END PROBLEM 3


    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
def wpm(typed, elapsed):
    assert elapsed > 0, 'Elapsed time must be positive'
    return (len(typed) / 5) / ( elapsed / 60)
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4


###########
# Phase 2 #
###########


    """Returns the element of VALID_WORDS that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        valid_words: a list of strings representing valid words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
def autocorrect(typed_word, valid_words, diff_function, limit):
    if typed_word in valid_words:
        return typed_word
    #自动检查字典中是否包含typed_word 键和值很重要
    min_diff = float('inf')
    min_word = typed_word
    for valid_word in valid_words:
        diff_word = diff_function(typed_word, valid_word, limit)
        if diff_word <= limit and min_diff > diff_word:
            min_diff = diff_word
            min_word = valid_word
    return min_word
    # END PROBLEM 5



    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_flips("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_flips("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_flips("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_flips("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_flips("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
def feline_flips(start, goal, limit):
    def helper(index1,index2,substitute):
        if steps > limit:
            return float('inf')
        if index1 >= len(start) or index2 >= len(goal):
            return substitute + abs(len(goal) - len(start))
        if start[index1] == goal[index2]:
            return helper(index1+1, index2+1 ,substitute)
        else:
            return helper(index1+1, index2+1 ,substitute+1)
    return helper(0,0,0)
    #第二种解法
    # result = helper(0,0,0)
    # return result if result <= limit else -1（表示无法完成）
    # END PROBLEM 6



#相信递归调用的方法,相信你传递回去的问题会被分解成无数的子问题

def minimum_mewtations(start, goal, limit):
    def helper(s,g, edits):
        if edits > limit:
            return float('inf')
        elif not s or not g:
            return edits + len(s) + len(g)
        elif s[0] == g[0]:
            return helper(s[1:], g[1:], edits)
        else:
            add = helper(s, g[1:] , edits+1)
            remove = helper(s[1:], g , edits+1)
            substitute = helper(s[1:], g[1:], edits+1)
            return min(add, remove , substitute)
    return helper(start,goal, 0) #返回初步调用的值





def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########



    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
def report_progress(sofar, prompt, user_id, upload):
    correct = 0
    for i in range(min(len(sofar), len(prompt))):
        if sofar[i] == prompt[i]:
            correct += 1
        else:
            break
    progress= correct / len(prompt) if len(prompt)>0 else 0.0
    upload({'id':user_id, 'progress':progress})
    return progress
    # END PROBLEM 8

###又是一个我不是很了解的数据结构

    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
def time_per_word(words, times_per_player):
    times = []
    for player_times in times_per_player:
        player_word_times = []
        for i in range(1,len(player_times)):
            player_word_times.append(player_times[i]-player_times[i-1])
        times.append(player_word_times)
    return {'words': words, 'times': times}
    # END PROBLEM 9
#重新定义 从字典中提取键
def get_words(match):
    return match['words']

def get_times(match):
    return match['times']

def time_per_word(words, times_per_player):
    times = []#大列表
    for player_times in times_per_player:
        player_word_times = []
        for i in range(1:len(player_times)):
            player_word_times.append(player_times[i]-player_times[i-1])
        times.append(player_word_times)
    
    return {
            'words': word, 
            'times': times
    }

def get_words(match):
    return match[words] #返回字典中的键所对应的值

def get_times(match):
    return match[times]
#形成字典形式

    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
def fastest_words(match):
    player_indices = range(len(get_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    #外层更新word 内层更新值
    fastest_players = []
    for player_word in word_indices: 
        min_times = float('inf')
        fastest_player = -1
        for player_id in player_indices:
            time = get_times(match)[player_id][player_word]
            if time < min_times:
                min_times = time
                fastest_player = player_id
            elif time == min_times:
                if player_id < fastest_player:
                    fastest_player = player_id
        fastest_players.append(fastest.player)
    return fastest_players

    #二层循环 更新 而不是那么复杂
    #循环取得数值-比较-更新

def fastest_words(match):
    player_indices = range(len(get_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_words(match)))    # contains an *index* for each word
    fastest_players = []
    for player_word in word_indices:
        fastest_player = -1
        min_time = float('inf')
        for player_id in player_indices:
            time = get_times(match)[player_id][player_word]
            if time < min_time:
                min_time = time 
                fastest_player = player_id
            elif time == min_time:
                if player_id < fastest_player:
                    fastest_player = player_id
        fastest_players.append(fastest_player)
    return fastest_players




    "*** YOUR CODE HERE ***"
    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(match, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(match[0]), "word_index out of range of words"
    return match[0][word_index]


def get_words(match):
    """A selector function for all the words in the match"""
    return match[0]


def get_times(match):
    """A selector function for all typing times for all players"""
    return match[1]


def time(match, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match[0]), "word_index out of range of words"
    assert player_num < len(match[1]), "player_num out of range of players"
    return match[1][player_num][word_index]


def match_string(match):
    """A helper function that takes in a match object and returns a string representation of it"""
    return "match(%s, %s)" % (match[0], match[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
