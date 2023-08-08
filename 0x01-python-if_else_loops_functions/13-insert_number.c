#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a node in a list
 * @head: first node
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current = *head, *pre = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
		*head = new_node;
	else
	{
		while (current->next && current->n <= number)
		{
			pre = current;
			current = current->next;
		}
		if (current->next == NULL && current->n <= number)
			current->next = new_node;
		else
		{
			pre->next = new_node;
			new_node->next = current;
		}
	}
	return (new_node);
}
