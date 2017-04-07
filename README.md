```
Filippo Mameli 6222254
filippo.mameli@stud.unifi.it
```

## N Grams
```
cd NGrams
```
#### Simple letter frequency (file, path)
`python letterCounter.py mobyDick.txt`

#### Histogram (n, option, file)
`python nGram.py 1 a mobyDick.txt`

#### nGram distribution (n, option, file)
`python nGram.py 4 b mobyDick.txt`

#### Index of coincidence and Entropy (n, option, file)
`python nGram.py 4 c mobyDick.txt`

## Hill Cypher
```
cd HillCypher
```
#### Crypt (PlainText, Key)
`python hill.py crypt friday htid`
#### Decrypt (Cyphertext, Key)
`python hill.py decrypt pqcfku htid`
#### CryptAnalysis (PlainText, Cyphertext, m)
`python hill.py cryptAnalysis friday pqcfku 2`

## Vigenere

#### Decrypt (keyLenght, file)
```
cd Vigenere
python vigenere.py 8 text.txt
```
