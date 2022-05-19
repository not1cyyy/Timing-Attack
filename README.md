Welcome to the Timing-Attack wiki!

# What are Timing Attacks ? 
According to Wikipedia.com, a timing attack is a [side-channel attack](https://en.wikipedia.org/wiki/Side-channel_attack) in which the attacker attempts to compromise a [cryptosystem](https://en.wikipedia.org/wiki/Cryptosystem) by analyzing the time taken to execute cryptographic algorithms. Every logical operation in a computer takes time to execute, and the time can differ based on the input; with precise measurements of the time for each operation, an attacker can work backwards to the input. Finding secrets through timing information may be significantly easier than using cryptanalysis of known plaintext, ciphertext pairs. Sometimes timing information is combined with cryptanalysis to increase the rate of information leakage 

# How do they work ? 
Suppose we have a password check mechanism (or even function) that checks whether the password is correct or not, if that function checks character by character with each iteration, it's most likely vulnerable to a timing attack, if you can measure the time required to return the error message with every input, you have a high chance of cracking the password 

# Why are they dangerous ? 
this password checking mechanism is still used in various products such as door locks or vault locks ... if someone with decent programming skills got to discover it's implemented, it's most likely that he'll break in 

# How does my simulation work ?
First, I'm simulating a database that has the username and the password. Then, I wrote a password check function that works exactly like it's supposed to work, checking every character at a time, and then with the help of other functions, I generated random strings with various sizes and calculated the response time to know which string is most likely to have the correct length, next, I tried every possible character and calculated the response time once again to know what character is most likely to be correct ! 
And so on and so fourth until cracking he full password ! 

# FAQ 
If you have any better idea/implementation, don't hesitate to contact me ! 