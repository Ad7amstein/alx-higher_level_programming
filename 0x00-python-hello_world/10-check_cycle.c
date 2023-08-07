#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle -  function in C that checks
 * if a singly linked list has a cycle in it.
 * @list: single list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *cur = list;

	if (list == NULL)
		return (0);
	while (cur->next)
	{
		if (cur->next == head)
			return (1);
		cur = cur->next;
	}
	return (0);
}
