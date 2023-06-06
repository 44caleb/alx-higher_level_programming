/**
*insert_node - inserts a node in a sorted list
*@head: adrress of pointer to start of node
*@number: number element in the node
*Return: the adress of node or NULL if error
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *pnext;
	listint_t *ptr = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;

	if ((ptr == NULL) || (number < ptr->n && ptr->next == NULL))
	{
		new_node->next = ptr;
		*head = new_node;
		return (new_node);
	}
	if ((number < ptr->n) && (ptr->next != NULL))
	{
		new_node->next = ptr;
		*head = new_node;
		return (new_node);
	}
	while (ptr != NULL)
	{
		pnext = ptr->next;

		if ((pnext == NULL) || ((number > ptr->n) && (number < pnext->n)))
		{
			new_node->next = pnext;
			ptr->next = new_node;
			return (new_node);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
