#include "lists.h"
/*
 * check_cycle - labala
 * @list: lol
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t = *m;
	listint_t = *o;

	m = list;
	o = list;
	while (list && m && m->next)
	{
		list = list->next;
		m = m->next;
		
		if (list == m)
		{
			list = o;
			o = m;
			while (1)
			{
				m = o;
				while (m->next != list && m->next != o)
				{
					m = m->next;
				}
				if (m->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
