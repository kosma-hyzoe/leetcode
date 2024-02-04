// https://leetcode.com/problems/valid-parentheses/
/*
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 *
 * An input string is valid if:
 *
 *     Open brackets must be closed by the same type of brackets.
 *     Open brackets must be closed in the correct order.
 *     Every close bracket has a corresponding open bracket of the same type.
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

#define OPEN_P	"({["
#define CLOSE_P	")}]"

struct stack {
	int top;
	char s[];
};

int char_in(char c, char *s)
{
	for (int i = 0; s[i] != '\0'; i++)
		if (s[i] == c)
			return 1;
	return 0;
}

int matches(char op, char cp)
{
	switch (op) {
		case '(':
			return cp == ')' ? 1 : 0;
		case '{':
			return cp == '}' ? 1 : 0;
		case '[':
			return cp == ']' ? 1 : 0;
		default:
			return -1;
	}
}

struct stack *stack_init(int len)
{
	struct stack *st = malloc(sizeof(struct stack) + len * sizeof(char));

	if (!st)
		exit(-1);

	st->top = -1;
	return st;
}


char stack_pop(struct stack *st)
{
	char c = st->s[st->top];
	st->top--;
	return c;
}

void stack_push(struct stack *st, char c)
{
	st->top++;
	*(st->s + st->top) = c;
}

char stack_get(struct stack *st)
{
	return st->s[st->top];
}

int stack_is_empty(struct stack *st)
{
	return st->top == -1;
}

bool isValid(char* s)
{
	char p;
	int len = strlen(s);
	struct stack *st = stack_init(len);

	if (char_in(*s, CLOSE_P)) {
			return false;
	}

	stack_push(st, *s);
	s++;

	while (*s) {
		p = *s;
		s++;
		if (char_in(p, OPEN_P))
			stack_push(st, p);

		if (st->top == -1) {
			return false;
		} else if (matches(stack_get(st), p)) {
			stack_pop(st);
		} else if (char_in(p, CLOSE_P)) {
			return false;
		}

	}

	if (!stack_is_empty(st))
			return false;
	free(st);
	return true;
}
