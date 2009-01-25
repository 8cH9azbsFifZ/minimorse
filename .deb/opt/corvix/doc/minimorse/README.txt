Mini-Morse
==========


Description
===========
This small python script will generate mp3 and corresponding text files
for learning / training the morse code. It follows the method (1) for
teaching the characters and the method described in (2) for improving
the skills even more. Parts of the code are based on this (3) very nice
program.
The morsed stuff will be spoken afterwards in the audio file :) 
Once the mp3s are generated, you may play them back on any mp3 player.
As meaningful id3 tags are inserted you easily may browse through all 
lessons even on a mobile phone.


Dependencies
============
- python
- lame
- espeak
- sox
- eyed3

Installation (corvix)
=====================
It will be installed under /opt/corvix/var/minimorse


Usage
=====
- Create kochs files:
     morse.py koch
  This will generate mp3s for learning the morse code from scratch. The
  koch method will be used with an effective farnsworth speed of 15wpm.
  The characters itself will be morsed at 25wpm.
- Create n0hffs files:
     morse.py n0hff
  This will generate mp3s for traning the morse code at the full 25wpm
  speed. The 100/500 most used words and pre/suffixes are availiable.
- Read the script and use it ;)


(1) Zeitschrift für angewandte Psychologie und Charakterkunde, Band 50 Heft 1 u. 2, Februar 1936:
      Arbeitspsychologische Untersuchung der Tätigkeit bei der Aufnahme von Morsezeichen, zugleich ein neues Anlernverfahren für Funker.
(2) William G. Pierpont N0HFF: The Art and Skill of Radio-Telegraphy
(3) KochMorse (C) Hannes Matuschek
