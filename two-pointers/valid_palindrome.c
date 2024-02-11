// https://leetcode.com/problems/valid-palindrome

#include <ctype.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int isPalindrome(char* s)
{
	char *l = s;
	char *r = s + strlen(s);

	while (l < r) {
		while (!isalnum(*l) && l < r)
			l++;
		while (!isalnum(*r) && l < r)
			r--;
		if (tolower(*(l++)) != tolower(*(r--)))
			return FALSE;
	}
	return TRUE;
}
