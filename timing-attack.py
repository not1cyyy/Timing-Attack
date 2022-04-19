import timeit
import itertools
import string
import numpy
import time
import random

database = {"not1cyyy": "jamescharlesfan69"}
Chars_to_use = string.ascii_lowercase + string.ascii_uppercase + " " + "." + "0123456789"

def check_password(user, guess):
    actual = database[user]
    if len(guess) != len(actual):
        return False

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            return False
    return True

def Generate_random_string(size):
    return ''.join(random.choices(Chars_to_use, k=size))

def crack_length(user, max_len=64, verbose=False) -> int:
    times = numpy.empty(max_len)
    trials = 2000
    for i in range(max_len):
        i_time = timeit.repeat(stmt='check_password(user, x)',
                               setup=f'user={user!r};x=Generate_random_string({i!r})',
                               globals=globals(),
                               number=trials,
                               repeat=10)
        times[i] = min(i_time)

    if verbose:
        most_likely_length = numpy.argsort(times)[::-1][:5]
        print(most_likely_length, times[most_likely_length] / times[most_likely_length[0]])

    most_likely = int(numpy.argmax(times))
    return most_likely

def crack_password(user, length, verbose=False):
    guess = Generate_random_string(length)
    trials = 1000
    counter = itertools.count()
    while True:
        i = next(counter) % length
        for c in Chars_to_use:
            alt = guess[:i] + c + guess[i + 1:]

            alt_time = timeit.repeat(stmt='check_password(user, x)',
                                     setup=f'user={user!r};x={alt!r}',
                                     globals=globals(),
                                     number=trials,
                                     repeat=10)
            guess_time = timeit.repeat(stmt='check_password(user, x)',
                                       setup=f'user={user!r};x={guess!r}',
                                       globals=globals(),
                                       number=trials,
                                       repeat=10)

            if check_password(user, alt):
                return alt

            if min(alt_time) > min(guess_time):
                guess = alt
                if verbose:
                    print(guess)


def main():
    user = "not1cyyy"
    length = crack_length(user, verbose=True)
    print(f"here's the most likely password length : {length}")
    input("ready to bruteforce ? hit enter ...")
    password = crack_password(user, length, verbose=True)
    print(f"here's the cracked password : {password}")
    print("see you again !")
    time.sleep(3)

if __name__ == '__main__':
    main()
