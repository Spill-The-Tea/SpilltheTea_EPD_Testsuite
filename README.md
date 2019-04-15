# SpilltheTea_EPD_Testsuite
A Repository of Chess Positions in EPD Format

## Testsuite WorkFlow
1. Create a Repository of freely available EPD Testsuites, unedited
2. Compile a single Large EPD Testsuite, of unique Positions from bulk Repository, Separate 'am' positions.
3. Analyze EPD Compilation using several engines, to create a selective EPD Testsuite of Very Difficult 'bm' Positions.
4. Validate those Positions (work in Progress).

## Secondary Goal of this Repository
5. Gather a Collection of Stockfish Losses, from Engine Matches, to better understand what went wrong.
6. Generate an EPD Testsuite from Engine Match Losses (work in Progress).

## Analysis Conditions
  * Hash = 1024 MB
  * Threads = 3
  * Engine = Stockfish 10, Xiphos 0.5, Ethereal 11.25, Laser 1.7, and Critter 1.6a

## Notes

After collecting a number of epd testsuites, you will begin to notice that every testsuite is </br>
incredibly incestuous. In most cases, using a simple awk expression through terminal was not sufficient </br>
to remove duplicates, because identical epd positions were reformatted (e.g. different IDs), and thus </br>
not removed properly. To overcome this, there is crude script written by Ferdinand Mosca in the Tools section </br>
of this repository, named "Remove_EPD_Duplicates.py."

## Sources and Links
 1. [Chess Programming](https://www.chessprogramming.org/Test-Positions), for general info about historically significant EPD Test Suites, and corresponding authors.
 2. [Arasan Testsuite](https://arasanchess.org/testsuite.shtml)
 3. [Arasan Engine EPD Repository](https://github.com/jdart1/arasan-chess/tree/master/tests)
 4. [Tactical Insanity Suite (Ti-c)](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32665) </br>
    a. This [Rybka Forum](http://rybkaforum.net/cgi-bin/rybkaforum/board_show.pl?tid=32659#tid32659) is also helpful
 5. [Strategic Test Suite](https://sites.google.com/site/strategictestsuite/download-all-epds-in-one-file)
 6. [Top-5000](http://web.archive.org/web/20180820213741/www.top-5000.nl/testsets.htm) used to host a repository </br>
 of various epd Testsuites, but is available through the web archive.
 7. [LaPuce Test Set (LCT-II)](https://www.chessprogramming.org/LCT_II)
 8. [Eigenmann Rapid Engine Test (ERET)](https://glarean-magazin.ch/2017/03/05/computerschach-testaufgaben-engines-eigenmann-rapid-engine-test-eret/)
 9. [Giraffe EPD Repository](https://github.com/AFDudley/giraffe/tree/master/tests/testsuites)
 10. [Hard Testsuite](http://www.talkchess.com/forum3/viewtopic.php?t=64914) by Vincent Lejeune (AKA Vinvin)
 11. [ClubFoot Repository](https://github.com/zd3nik/Clubfoot/tree/master/epd)
 12. [Collection of Old EPD Test Suites](http://computer-chess.org/doku.php?id=computer_chess:wiki:download:index), also included in top-5000 collection.
 13. [Protector EPD Repository](https://sourceforge.net/p/protector/code/HEAD/tree/epd/)
 14. [ECM Testsuite](http://web.archive.org/web/20180714035646/http://www.st.ewi.tudelft.nl/~renze/doc/TestSuites/ECM.epd)
 15. [Zugzwangs](https://www.stmintz.com/ccc/index.php?id=391553)
 16. [Colditz Suite](http://www.talkchess.com/forum3/viewtopic.php?t=62659)
 17. [Quick Test Set](http://members.aon.at/computerschach/quick/quick.epd)
 18. [BlitzChess Sources](http://www.blitzchess.fr/fr/tests/index.html)
 19. 
 
 
 
