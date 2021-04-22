#include <bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	struct node* next;
};

void printMiddle(struct node* head)
{
	int count = 0;
	struct node *mid = head;
	
	while (head != NULL)
	{
		if (count&1)
			mid = mid->next;
		count++;
		head = head->next;
	}
	
	if (mide != NULL)
		printf("The middle element is [%d]\n\n",
				mid->data);
}
