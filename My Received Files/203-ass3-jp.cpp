//Jonathan Pentecost

#include<iostream>
#include<fstream>
using namespace std;

struct Node{
	int node1,node2,span;//span is the same as cost
	Node *next;
	bool visited;// is true only when it has been visited
};

int main(int argc,char *argv[])
{	
	char fname[50];
	for (int x=0;x<50;x++)
		fname[x] = argv[1][x];
	srand ( time(NULL) );


	Node *first,*current,*newNode,*Temp;
	//char fname[] = "graph.txt";
	int num_Nodes,count = 0;
	int buffer=0;
	first = NULL;
	
	ifstream fin;
	fin.open(fname);
	
	if (fin.good())
	{
	
		fin >> num_Nodes;
	
		while (!fin.eof())
		{
			newNode=new Node;
			fin >> buffer;
			newNode->node1=buffer;
			fin >> buffer;
			newNode->node2=buffer;
			fin >> buffer;
			if (buffer == 0)// breaks when the cost/span gets to 0 because you can't have a span or cost = 0
			{
				delete newNode;
				break;
			}
			newNode->span = buffer;
			newNode->next=NULL;
			newNode->visited = false;
			if (first==NULL)
			{
				first=newNode;
			}
			else
			{
				current=first;
				if (current->next!=NULL)
				{
					while(current->next!=NULL)
					{
						current = current->next;
					}
					current->next=newNode;
				}
				else
				{
					current->next=newNode;
				}
				
			}
			count++;
			
		}
		fin.close();
	}
	else
	{
 	    	cerr << "bad file" << endl;
	}
	
	//-------------starting prims algorithm----------
	int current_Nodes[num_Nodes], cur_num_nodes = 1;//cur_num_nodes is an iterator for current_Nodes [] array
	int ran = rand()%num_Nodes+1;//gets a random starting point
	int tot_span = 0;
	cout << "The starting point for this graph is " << ran << endl;
	current_Nodes[0] = ran;
	int least;//setting least to highest possibly value so everything will be smaller that it
	int least_pos, pos;
	for (int y=0;y<count;y++)
	{
		pos = 0;
		least = 999999;
		current = first;
		while (current!=NULL)//runs through the linkedlist finding the least value.
		{
			if (!current->visited)
			{
				for (int x=0;x<cur_num_nodes;x++)
				{
					if (current_Nodes[x] == current->node1)
					{
						if (current->span < least)
						{
							least = current->span;
							least_pos = pos;
						}
					}
					if (current_Nodes[x] == current->node2)
					{
						if (current->span < least)
						{
							least = current->span;
							least_pos = pos;
						}
					}
				}
			}
			current = current->next;
			pos++;
		}
		current = first;
		for (int x=0;x<least_pos;x++)//going through untill the node with the smallest span is found
		{
			current = current->next;
		}
		current->visited = true;
		bool one = false, two = false;//booleans to check to see if current->nodes are in the current_Node[] array
		for (int x=0;x<cur_num_nodes;x++)//for loop checking to see if current->node is already in current_Node[] if not add it to current_Node array
		{
			if (current_Nodes[x] != current->node1)
			{
				one = true;
			}
			if (current_Nodes[x] != current->node2)
			{
				two = true;
			}
		}
		if (one)
		{
			current_Nodes[cur_num_nodes] = current->node1;
			cur_num_nodes++;
		}
		if (two)
		{
			current_Nodes[cur_num_nodes] = current->node2;
			cur_num_nodes++;
		}
		cout << "Node 1: " << current->node1 << " Node2: " << current->node2 << " Span: " << current->span << endl;	
		tot_span += current->span;
	}
	cout << "The total span taken is: " << tot_span << endl;
	
}
