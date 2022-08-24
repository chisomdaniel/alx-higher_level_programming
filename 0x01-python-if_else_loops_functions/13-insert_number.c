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
	listint_t *headptr = *head, nextptr = headptr, *new;

	new->n = number;

	while (nextptr != NULL)
	{
		if (number <= nextptr->n || nextptr->n == NULL)
		{
			new->next = nextptr->next;
			nextptr->next = new;
			return (new);
		}
		nextptr = nextptr->next;
	}

	/*If no place is found for the element, fix it at the beginning */
	new->n = headptr;
	*head = new;

	return (new);
}
