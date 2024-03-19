# JSON Parser

[Coding challenges](https://codingchallenges.fyi/challenges/challenge-json-parser/)

## Unit Tests

```Bash
pytest -q json_parser_test.py
```

## Functional Tests

* Failures

```Bash
for i in {1..33}; do cat test/fail$i.json | python json_parser.py ; if [[ $? -eq 0 ]] ;then echo "Success exit code: $?"; else echo "Error exit code $?" ;fi; done
```

* Success

```Bash
for i in {1..3}; do cat test/pass$i.json | python json_parser.py ; if [[ $? -eq 0 ]] ;then echo "Success exit code: $?"; else echo "Error exit code $?" ;fi; done
```
