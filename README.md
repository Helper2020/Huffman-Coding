# Huffman-Coding
Show Me The Data Structures

Overview - Data Compression
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.

A. Huffman Encoding
Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:
