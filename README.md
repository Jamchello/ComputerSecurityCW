# ComputerSecurityCW

This repository contains Python scripts that were written during the completion of the Computer Secruity Module's coursework:
  1. A script that breaks a weak RSA encryption under the constraint that p and q were selected poorly and are close to one another.
  Because n = p * q and the difference between them must be less than 10000, it is possible to narrow the possible space of values to 10000: (√𝑛−5000…√𝑛+5000).
  From this point onwards, the code steps iteratively through each possible value of p (p?) in this range, if n%(p?) = 0 and it is also a prime, then it is one of the prime factors.
  The value of q can then be obtained by doing the calculation of n/p. Equipped with the values of n,p,q and e it is possible to calculate the private key.
 
  2. A pair of python scripts that can be utilised together to perform a diffie hellman to produce a shared key for encryption.
