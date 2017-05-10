#!/usr/bin/python/
import actual_dictionary_make

dictionary = [False]*26

if __name__ == "__main__":
	input1 = open("input2.txt" , 'r')
	dic_yet = ""
	print("Building dictionary")
	for chunk in input1:
		dic_yet+=chunk
		actual_dictionary_make.	add_to_dictionary(dictionary , dic_yet)
	print("Done")
	while True:
		word = raw_input("Enter a word: ")
		print( actual_dictionary_make.check_else_find(dictionary , word) )