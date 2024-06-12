# Unix WC Tool

ccwc.py is a command line tool built to display the number of lines, words, and bytes contained in each input file.

### Usage

- ccwc.py [-h] [-c] [-l] [-w] [-m] filename

### Positional arguments:

- filename The number of bytes, lines, and words from input file.

### options:

- -h, --help show this help message and exit
  <br>
- -c The number of bytes in each input file is written to the standard output.
  <br>
- -l The number of lines in each input file is written to the standard output.
  <br>
- -w, -word The number of words in each input file is written to the standard output.
  <br>
- -m, -char The number of characters in each input file is written to the standard output.

### Example

Input: `python ccwc.py test.txt`
<br>
Output `7145 58164 342190 test.txt`
<br>
<br>
Input: `python ccwc.py -l test.txt`
<br>
Output `7145 test.txt`

### Credit

Unix WC Tool challenge provided by **[John Crickett](https://www.linkedin.com/in/johncrickett/)**
<br>
Challenge Instructions **[HERE](https://codingchallenges.fyi/challenges/challenge-wc)**
