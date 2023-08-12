#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *tmp = NULL;
	int size = 0, i = 0, j = 0;

	if (*head == NULL)
		return (1);
	while (current)
	{
		size++;
		current = current->next;
	}
	if (size == 1)
		return (1);
	current = *head;
	for (i = 0; i < size / 2; ++i)
	{
		tmp = current;
		for (j = i; j < size - 1 - i; ++i)
			tmp = tmp->next;
		if (current->n != tmp->n)
			return (0);
		current = current->next;
	}
	return (1);
}
