#include <stddef.h>
#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - a function to insert a node in a sorted singly linked list
 *
 * @head: the start of the array
 * @number: the number to add
 *
 * Return: a pointer to the new element
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *headptr = *head, *prev = headptr, *nextptr = headptr, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (nextptr != NULL)
	{
		if (number <= nextptr->n)
		{
			new->next = nextptr;
			if (prev == headptr)
			{
				*head = new;
				return (new);
			}
			prev->next = new;
			return (new);
		}
		if (nextptr->next == NULL)
		{
			nextptr->next = new;
			new->next = NULL;
			return (new);
		}
		prev = nextptr;
		nextptr = nextptr->next;
	}

	/*If no place is found for the element, fix it at the beginning */
	new->next = headptr;
	*head = new;

	return (new);
}
