// https://leetcode.com/problems/valid-palindrome

#include <ctype.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int isPalindrome(char* s)
{
	int l = 0;
	int r = strlen(s) - 1;

	while (l < r) {
		while (!isalnum(s[l]) && l < r)
			l++;
		while (!isalnum(s[r]) && l < r)
			r--;
		if (tolower(s[l++]) != tolower(s[r--]))
			return FALSE;
	}
	return TRUE;
}
