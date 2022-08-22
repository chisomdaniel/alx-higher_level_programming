#include "lists.h"

/**
 * check_cycle - a function that detects cycle in a linked list
 *
 * @list: the list
 *
 * Return: 0 if no cycle, 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint *nextptr, *nexttwo;

	nextptr = nexttwo = list;

	while (next != NULL)
	{
		nextptr = nextptr->next;
		nexttwo = nexttwo->next->next;

		if (nextptr == nexttwo)
		{
			return (1);
		}
	}

	return (0);
}
