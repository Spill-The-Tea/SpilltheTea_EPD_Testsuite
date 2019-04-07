# SpilltheTea_EPD_Testsuite
A Repository of Chess Positions in EPD Format

## Testsuite WorkFlow
1. Create a Repository of freely available EPD Testsuites, unedited
2. Compile a single Large EPD Testsuite, of unique Positions from bulk Repository, Exclude 'am' positions
3. Analyze EPD Compilation, to create a selective EPD Testsuite of Very Difficult 'bm' Positions
4. Validate those Positions (work in Progress)
5. Analyze difficult, but Validated positions with engines other than stockfish to identify positions
difficult to a variety of engines.

## Secondary Goal of this Repository
6. Gather a Collection of Stockfish Losses, from Engine Matches, to better understand what went wrong.
7. Generate an EPD Testsuite from Engine Match Losses.

## Analysis Conditions
  * Hash = 1024 MB
  * Threads = 3
  * Engine = Stockfish 10
  * Subsequent analysis uses other engines: Xiphos 0.5, Fire 7.1, Ethereal 11.25, and Komodo 11.3

## Notes
After collecting a number of epd testsuites, you will begin to notice that every testsuite is </br>
incredibly incestuous. In most cases, using a simple awk expression through terminal was not sufficient </br>
to remove duplicates, because identical epd positions were reformatted (e.g. different IDs), and thus </br>
not removed properly. The easiest way to overcome this, is to strip all fields, except the fen string, </br>
and perpetuate the problem I am describing, by renaming them later.

In other cases, I have observed identical positions, with different best moves (bm), both of which were </br>
horribly wrong. This repository, is hoping to reduce these two problems among test suites. 

## Sources and Links
 1. [Arasan Testsuite](https://arasanchess.org/testsuite.shtml)
 2. [Arasan Engine EPD Repository](https://github.com/jdart1/arasan-chess/tree/master/tests)
 2. [Tactical Insanity Suite (Ti-c)](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32665) </br>
    a. This [Rybka Forum](http://rybkaforum.net/cgi-bin/rybkaforum/board_show.pl?tid=32659#tid32659) is also helpful
 3. [Strategic Test Suite](https://sites.google.com/site/strategictestsuite/download-all-epds-in-one-file)
 4. [Top-5000](http://web.archive.org/web/20180820213741/www.top-5000.nl/testsets.htm) used to host a repository </br>
 of various epd Testsuites, but is available through the web archive.
 5. [LaPuce Test Set (LCT-II)](https://www.chessprogramming.org/LCT_II)
 6. [Eigenmann Rapid Engine Test (ERET)](https://glarean-magazin.ch/2017/03/05/computerschach-testaufgaben-engines-eigenmann-rapid-engine-test-eret/)
 7. [Giraffe EPD Repository](https://github.com/AFDudley/giraffe/tree/master/tests/testsuites)
 8. [Hard Testsuite](http://www.talkchess.com/forum3/viewtopic.php?t=64914) by Vincent Lejeune (AKA Vinvin or Dorszcz)
 9. [ClubFoot Repository](https://github.com/zd3nik/Clubfoot/tree/master/epd)
 10. [Collection of Old EPD Test Suites](http://computer-chess.org/doku.php?id=computer_chess:wiki:download:index), also included in top-5000 collection.
 11. [Protector EPD Repository](https://sourceforge.net/p/protector/code/HEAD/tree/epd/)
 12. 
 
