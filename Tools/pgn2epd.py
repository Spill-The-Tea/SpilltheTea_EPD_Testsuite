#!/usr/bin/env python3

### A simple, yet useful Python Script to Convert a PGN File (Test Suites) to
### EPD compatible format, by taking the first move in the file as the Best
### Move.
###
### The FEN String is taken from the FEN Tags. Unfortunately, this does not 
### take any other information associated with positions, such as an ID...
###
### Script taken from tools folder of the Giraffe Engine created by Matthew Lai
### https://bitbucket.org/waterreaction/giraffe/src/d3aa7af342db8b0b254f030d5ca5b674b5f83181/tools/pgn2epd.py?at=default&fileviewer=file-view-default

import chess
import sys

from chess import pgn

if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " <PGN file>")
	sys.exit(1)

if sys.argv[1] == '-':
    pgn = sys.stdin
else:
    pgn = open(sys.argv[1])

game = chess.pgn.read_game(pgn)
while game != None:
	
	gameNode = game
	while len(gameNode.variations):
		print(gameNode.board().epd(bm = gameNode.variations[0].move))
		gameNode = gameNode.variations[0]
	
	game = chess.pgn.read_game(pgn)
