#include "lists.h"
/**
 * reverse - fcxdzsa
 * @h_r: vfcdx
 * Return: uikj
 */
void reverse(listint_t **h_r)
{
	listint_t *ik;
	listint_t *uo;
	listint_t *bn;

	ik = NULL;
	uo = *h_r;

	while (uo != NULL)
	{
		bn = uo->next;
		uo->next = ik;
		ik = uo;
		uo = bn;
	}

	*h_r = ik;
}

/**
 * compare - vgcfccfxd
 * @h1: xdzsa
 * @h2: vgcfdx
 * Return: vcx
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *cx1;
	listint_t *cx2;

	cx1 = h1;
	cx2 = h2;

	while (cx1 != NULL && cx2 != NULL)
	{
		if (cx1->n == cx2->n)
		{
			cx1 = cx1->next;
			cx2 = cx2->next;
		}
		else
		{
			return (0);
		}
	}

	if (cx1 == NULL && cx2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - bhgv
 * @head: iokl
 * Return: okl
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
