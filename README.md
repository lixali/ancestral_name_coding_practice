# ancestral_name_coding_practice

Ancestral NamesIn some cultures, children are named after ancestors and there is a number 
following which represents how many ancestors have shared that name. 
They are often shown as Roman Numerals. 
In Roman numerals, a value is not repeated more than three times. 
At that point, a smaller value precedes a larger value to indicate subtraction. 
For example, the letter I represents the number 1, and V represents 5. Reason through the formation of 1 to 10 below, 
and see how it is applied in the following lines. I, II, III, IV, V, VI, VII, VIII, IX, and X represent 1 through 10.
XX, XXX, XL, and L are 20, 30, 40, and 50.For any other two-digit number < 50, 
concatenate the Roman numeral(s) that represent its multiples of ten with the Roman numeral(s) for its values < 10. 
For example, 43 is 40 + 3 = "XL" + "III" = "XLIII" Given a list of strings comprised of a name and a Roman numeral, 
sort the list first by name, then by decimal value of the Roman numeral. For example, 
if you are given the names [Steven XL, Steven XVI, David IX, Mary XV, Mary XIII, Mary XX] 
the result of the sort is [David IX, Mary XIII, Mary XV, Mary XX, Steven XVI, Steven XL]. 
The result with Roman numerals is the expected return value. Written with the numbers in decimal, 
they are [David 9, Mary 13, Mary 15, Mary 20, Steven 16, Steven 40]. 

Function Description Complete the function sortRoman in the editor below. 
The function must return the array sorted first by given name, then by ordinal. 
sortRoman has the following parameter: names[names[0],...names[n-1]]: 
an array of strings Constraints1 ≤ n ≤ 50Each names[i] is a single string composed of 2 space-separated values: 
givenName and romanNumeral.romanNumeral represents a number between 1 and 50, 
inclusive.1 ≤ |givenName| ≤ 20Each givenName starts with an uppercase letter ascii[A-Z] 
which is followed by lowercase letters ascii[a-z].
There is a space between givenName and romanNumeralEach names[i] is distinct.

Sample Input 
2
Louis IX
Louis VIII 

Sample Output
Louis VIII Louis IX

Explanation 0Sort first by givenName then, 
if givenName is not unique, by value of the Roman numeral. 
In decimal, the list is sorted [Louis 8, Louis 9].
