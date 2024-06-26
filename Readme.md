## Luhn Algorithm Digit Sequence Checksum Calculator

- Dependencies      : Json,flask_cors,Flask
- To run the server : python server.py

## About the Luhn Algorithm
This calculator computes the digit sequence checksum using the Luhn algorithm (mod 10) and provides the validation digit. The Luhn algorithm, developed by German computer scientist Hans Peter Luhn in 1954, is a simple checksum formula used to validate identification numbers like credit card numbers.
The Luhn algorithm is designed to detect accidental errors, such as digit mistyping, in identification numbers. 
## How to Use
- Enter the digit sequence in the input field.
- Click the “Validate” button to calculate the checksum.
- The result will show whether the sequence is valid or not.
- If the sequence is not valid, we can check the next check digit to make the sequence valid by clicking 'Check digit'.

## Example
  Suppose you have a digit sequence like “123456789”. 
  Upon validation, if the checksum is not zero, the calculator will suggest the next check digit to append to the sequence to make it valid according to the Luhn algorithm.

## Note
This calculator serves as a handy tool for verifying the integrity of identification numbers, 
especially credit card numbers, using the Luhn algorithm.
