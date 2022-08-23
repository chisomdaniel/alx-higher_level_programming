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
	listint_t *nextptr, *nexttwo;

	nextptr = nexttwo = list;

	while (nextptr != NULL && nexttwo != NULL)
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
