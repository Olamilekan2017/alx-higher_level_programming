#include "lists.h"

/**
 * check_cycle - This checks if a singly list has a cycle in it
 * @list: The only parameter
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return(0);
	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
		return(1);
		}
	}
	return (0);
}
