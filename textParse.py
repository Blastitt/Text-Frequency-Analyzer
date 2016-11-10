#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import string

class Parser():
	def __init__(self, textDirectory, outFileName):
		funkyLetters = [u"ä", u"ö", u"ü", u"ñ"]
		self.alphabet = list(string.ascii_uppercase) + funkyLetters
		


		self.textDirectory = textDirectory
		self.files = os.listdir(textDirectory)
		self.outFile = outFileName

		self.characters = {}
		self.pairs = {}
		self.triplets = {}

		self.totalSingle = 0
		self.totalDouble = 0
		self.totalTriple = 0
		self.totalFiles = 0

	def parseFile(self, fileName):

		self.parseFileSingle(fileName)
		self.parseFileDouble(fileName)
		self.parseFileTriple(fileName)

	def parseFileSingle(self, fileName):
		fileName = "%s/%s" % (self.textDirectory, fileName)
		with open(fileName, 'r') as f:
			while True:
				c = f.read(1)
				if not c:
					f.close()
					print "Done reading LETTERS from file: ", fileName
					self.totalFiles += 1
					break

				c = c.upper()

				if c in list(string.ascii_uppercase):
					self.totalSingle += 1

					if c not in self.characters:
						self.characters[c] = 0

					self.characters[c] += 1

	def parseFileDouble(self, fileName):
		fileName = "%s/%s" % (self.textDirectory, fileName)
		with open(fileName, 'r') as f:
			while True:
				c = f.read(2)
				if not c or len(c) < 2:
					f.close()
					print "Done reading PAIRS from file: ", fileName
					break

				c = c.upper()

				if c[0] in self.alphabet and c[1] in self.alphabet:
					self.totalDouble += 1

					if c not in self.pairs:
						self.pairs[c] = 0

					self.pairs[c] += 1

				f.seek(-1, 1) # Move file cursor back 1 byte to get all letter pairs.

	def parseFileTriple(self, fileName):
		fileName = "%s/%s" % (self.textDirectory, fileName)
		with open(fileName, 'r') as f:
			while True:
				c = f.read(3)
				if not c or len(c) < 3:
					f.close()
					print "Done reading TRIPLETS from file: ", fileName
					break

				c = c.upper()

				if c[0] in self.alphabet and c[1] in self.alphabet and c[2] in self.alphabet:
					self.totalTriple += 1

					if c not in self.triplets:
						self.triplets[c] = 0

					self.triplets[c] += 1

				f.seek(-2, 1) # Move file cursor back 2 bytes to get all letter triplets.

	def startParse(self):
		for fileName in self.files:
			self.parseFile(fileName)

	def outputResults(self):

		with open("SINGLE-"+self.outFile, 'w') as out:
			out.write("Total Files: %d\n" % self.totalFiles)
			out.write("Total Patterns: %d\n" % self.totalSingle)
			for character, frequency in self.characters.iteritems():
				out.write("%s,%d\n" % (character, frequency))

		with open("PAIRS-"+self.outFile, 'w') as out:
			out.write("Total Files: %d\n" % self.totalFiles)
			out.write("Total Pairs: %d\n" % self.totalDouble)
			for pair, frequency in self.pairs.iteritems():
				out.write("%s,%d\n" % (pair, frequency))

		with open("TRIPLETS-"+self.outFile, 'w') as out:
			out.write("Total Files: %d\n" % self.totalFiles)
			out.write("Total Triplets: %d\n" % self.totalTriple)
			for triplet, frequency in self.triplets.iteritems():
				out.write("%s,%d\n" % (triplet, frequency))


def main():
	directory = sys.argv[1]
	outfile = sys.argv[2]

	p = Parser(directory, outfile)

	p.startParse()
	p.outputResults()

if __name__ == "__main__":
	main()