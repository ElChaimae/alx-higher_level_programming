#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *tmp;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (is_palindrome);

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
tmp = slow->next;
slow->next = prev;
prev = slow;
slow = tmp;
}

if (fast != NULL)
slow = slow->next;

while (slow != NULL)
{
if (prev->n != slow->n)
{
is_palindrome = 0;
break;
}
prev = prev->next;
slow = slow->next;
}

fast = prev;
prev = NULL;

while (fast != NULL)
{
tmp = fast->next;
fast->next = prev;
prev = fast;
fast = tmp;
}

(*head)->next = prev;

return (is_palindrome);
}

