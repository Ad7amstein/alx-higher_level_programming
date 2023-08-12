#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *tmp = NULL;
	int size = 0, i = 0, j = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (current)
	{
		size++;
		current = current->next;
	}
	current = *head;
	for (i = 0; i < size / 2; ++i)
	{
		tmp = current;
		for (j = i; j < size - 1 - i; ++j)
			tmp = tmp->next;
		if (current->n != tmp->n)
			return (0);
		current = current->next;
	}
	return (1);
}
