from __future__ import annotations

__author__ = "Benjamin Robillard"
__class__ = "CSCI 375 - 001"
__assignment__ = "A7 Kattis Problem using ABC"

from abc import ABC, abstractmethod
from typing import Any
from kattis import Kattis
from cup import Cup
import sys

class Main(Kattis):
	""" This class is used to handle the reading of input given from kattis/user
	input and solving the kattis problem (stacking cups). It formats the answer
	and prints it to the console for kattis to check the solution.

	Args:
		Kattis: Kattis abstract based class
	"""
	def __init__(self, data_source: Any = sys.stdin) -> None:
		""" initializing Main class to handle reading input, solving the problem, formatting and printing the answer

		Args:
			data_source (Any, optional): reading input from sys.stdin from user. Defaults to sys.stdin.
		"""
		super().__init__(data_source)
		self._data:list[str] = []
		self._answer:list[str] = []
		self.read_input()

	def read_input(self) -> None:
		""" Reading input given from data file or user input
		"""
		data = self._input_source.readlines()
		for line in data:
			self._data.append(line.rstrip().split())
			# print(self._data)
		# print(self._data)

	def data(self) -> Any:
		""" Data method to return the data given from user or data file 

		Returns:
			Any: list[[int or str, int or str], [int or str, int or str], ...]
		"""
		return self._data

	@property
	def answer(self) -> Any:
		""" Formatting _answer so that kattis will accept the answer

		Returns:
			Any: formatted answer gotten from Main.solve 
		"""
		return '\n'.join([str(t) for t in self._answer])

	def solve(self) -> None:
		""" Solve method used to find answer gotten from Cup.is_int() and uses what it 
		returns to know what to append to sorted_cups. sorted_cups is then sorted and assigned to 
		_answer attribute for later use
		"""
		sorted_cups = []
		for line in self._data[1:]:
			cup = Cup(line)
			if cup.is_int():
				sorted_cups.append((int(line[0]), line[1]))
			else:
				sorted_cups.append((2 * int(line[1]), line[0]))
		sorted_cups = sorted(sorted_cups)
		# print(sorted_cups)
		for pair in sorted_cups:
			self._answer.append(pair[1])
		self._answer.append("")


	def print_answer(self) -> None:
		""" Printing answer to console
		"""
		sys.stdout.write(str(self.answer))
		

if __name__ == "__main__":
	""" Running Main class
	"""
	solution = Main()
	solution.solve()
	solution.print_answer()
