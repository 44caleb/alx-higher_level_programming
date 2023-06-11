#include "lists.h"

int is_palindrome(listint_t **head);
int len_list(listint_t **head);

/**
*is_palindrome - checks if a linked list is a palindrome
*@head: address of pointer to the head of list
*Return: 1 if palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int len, i = 0, j = 0;
	int list_array[100];

	if (ptr == NULL)
	{
		return (1);
	}

	len = len_list(head);

	for (i = 0; i < len; i++)
	{
		list_array[i] = ptr->n;
		ptr = ptr->next;
	}

	while (j < len)
	{
		if (list_array[j] != list_array[i - 1])
		{
			return (0);
		}
		j++;
		i--;
	}
	return (1);
}


/**
*len_list - gets the number of elements in a list
*@head: address to pointer to head of list
*Return: number of elements
*/
int len_list(listint_t **head)
{
	listint_t *ptr = *head;
	int len = 0;

	while (ptr != NULL)
	{
		len++;
		ptr = ptr->next;
	}
	return (len);
}
