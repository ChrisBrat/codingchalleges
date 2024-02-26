# WC

[Coding challenges](https://codingchallenges.fyi/challenges/challenge-wc/)

## Options

* `-l` = Number of lines
* `-w` = Number of words
* `-c` = Number of bytes
* `-m` = Number of characters

## Usage

### File argument

```Bash
python wc.py <option> <filename>
```

#### Examples

```Bash
python wc.py -l test.txt
```

```Bash
python wc.py -w test.txt
```

```Bash
python wc.py -c test.txt
```

```Bash
python wc.py -m test.txt
```

```Bash
python wc.py test.txt
```

### Input stream

```Bash
cat <filename> | python wc.py <option>
```

#### Examples

```Bash
cat test.txt | python wc.py -l
```

```Bash
cat test.txt | python wc.py -w
```

```Bash
cat test.txt | python wc.py -c
```

```Bash
cat test.txt | python wc.py -m
```

```Bash
cat test.txt | python wc.py
```

## Issues

* ~~stdin contents not read when arguments used.~~ [Updated to use `sys.stdin.buffer` and `line.decode()`]
* ~~Encoding difference between stdin and file open causes different byte results.~~  [Updated to read binary file and use `line.decode()`]
