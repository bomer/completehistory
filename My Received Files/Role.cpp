//JOnathan Pentecost
//204-assignment 2
// funcrtions

#include<iostream>
#include<fstream>
using namespace std;
#include"Role.h"

void Characteristics::setCharacteristics(string Name, int s,int i,int w, int d, int co, int ch){
	name=Name;
	Strength=s;
	Intellegence=i;
	Wisdom=w;
	Dexterity=d;
	Constitution=co;
	Charisma=ch;
	cout << "A:" << name << endl;	
}

Race::Race(){
	Node *current,*newNode;
	char fname[15]={"Races.txt"};
	first = NULL;
	string junk;
	int count=0;
	ifstream fin;
	fin.open(fname);
	if (!fin.good())
		cout << "error" << endl;
	else
	{
		while (!fin.eof())
		{
			newNode=new Node;
			getline(fin,newNode->name,':');
			fin >> newNode->Strength;
			fin.ignore(1);
			fin >> newNode->Intellegence;
			fin.ignore(1);
			fin >> newNode->Wisdom;
			fin.ignore(1);
			fin >> newNode->Dexterity;
			fin.ignore(1);
			fin >> newNode->Constitution;
			fin.ignore(1);
			fin >> newNode->Charisma;
			getline(fin,junk,'\n');
			newNode->next=NULL;
			if (first==NULL)
				first=newNode;
			else
			{
				current=first;
				if (current->next!=NULL)
				{
					while(current->next!=NULL)
						current=current->next;
					current->next=newNode;
				}
				else
				current->next=newNode;
				
			}
			count++;
		
		}
	}
	srand((unsigned)time(NULL));
	int ran_num=rand()%count;

	current=first;
	for (int x=0;x<ran_num-1;x++)
		current=current->next;	
	ch.setCharacteristics(current->name,current->Strength,current->Intellegence,current->Wisdom,current->Dexterity,current->Constitution,current->Charisma);
	p.setPerson(current->name);	
}

void Person::setPerson(string r)
{
	name="vishen";
	race=r;
	cout << name << " " << race << endl;
}

Helmets::Helmets(){
	Node *current,*newNode;
	char fname[15]={"Helmets.txt"};
	string junk;
	first = NULL;
	int count=0;
	ifstream fin;
	fin.open(fname);
	if (!fin.good())
		cout << "error" << endl;
	else
	{
		while (!fin.eof())
		{
			newNode=new Node;
			getline(fin,newNode->name,':');
			fin >> newNode->minArmour;
			fin.ignore(1);
			fin >> newNode->maxArmour;
			fin.ignore(1);
			fin >> newNode->maxArmour_magical;
			fin.ignore(1);
			fin >> newNode->weight;
			getline(fin,junk,'\n');
			newNode->next=NULL;
			cout << "!: " << newNode->name << " " << newNode->minArmour << " " << newNode->maxArmour << " " << newNode->maxArmour_magical << " " << newNode->weight << endl;
			if (first==NULL)
				first=newNode;
			else
			{
				current=first;
				if (current->next!=NULL)
				{
					while(current->next!=NULL)
						current=current->next;
					current->next=newNode;
				}
				else
				current->next=newNode;
				
			}
			count++;
		
		}
	}
}

Shields::Shields(){
	Node *current,*newNode;
	char fname[15]={"Shields.txt"};
	string junk;
	first = NULL;
	int count=0;
	ifstream fin;
	fin.open(fname);
	if (!fin.good())
		cout << "error" << endl;
	else
	{
		while (!fin.eof())
		{
			newNode=new Node;
			getline(fin,newNode->name,':');
			fin >> newNode->minArmour;
			fin.ignore(1);
			fin >> newNode->maxArmour;
			fin.ignore(1);
			fin >> newNode->maxArmour_magical;
			fin.ignore(1);
			fin >> newNode->weight;
			getline(fin,junk,'\n');
			newNode->next=NULL;
			cout << "!: " << newNode->name << " " << newNode->minArmour << " " << newNode->maxArmour << " " << newNode->maxArmour_magical << " " << newNode->weight << endl;
			if (first==NULL)
				first=newNode;
			else
			{
				current=first;
				if (current->next!=NULL)
				{
					while(current->next!=NULL)
						current=current->next;
					current->next=newNode;
				}
				else
				current->next=newNode;
				
			}
			count++;
		
		}
	}
}

Armour::Armour(){
	Node *current,*newNode;
	char fname[15]={"Armour.txt"};
	string junk;
	first = NULL;
	int count=0;
	ifstream fin;
	fin.open(fname);
	if (!fin.good())
		cout << "error" << endl;
	else
	{
		while (!fin.eof())
		{
			newNode=new Node;
			getline(fin,newNode->name,':');
			fin >> newNode->minArmour;
			fin.ignore(1);
			fin >> newNode->maxArmour;
			fin.ignore(1);
			fin >> newNode->maxArmour_magical;
			fin.ignore(1);
			fin >> newNode->weight;
			getline(fin,junk,'\n');
			newNode->next=NULL;
			cout << "!: " << newNode->name << " " << newNode->minArmour << " " << newNode->maxArmour << " " << newNode->maxArmour_magical << " " << newNode->weight << endl;
			if (first==NULL)
				first=newNode;
			else
			{
				current=first;
				if (current->next!=NULL)
				{
					while(current->next!=NULL)
						current=current->next;
					current->next=newNode;
				}
				else
				current->next=newNode;
				
			}
			count++;
		
		}
	}
}

Weapons::Weapons(){
	Node *current,*newNode;
	char fname[15]={"Weapons.txt"};
	string junk;
	first = NULL;
	int count=0;
	ifstream fin;
	fin.open(fname);
	if (!fin.good())
		cout << "error" << endl;
	else
	{
		while (!fin.eof())
		{
			newNode=new Node;
			getline(fin,newNode->name,':');
			fin >> newNode->diceTimes;
			fin.ignore(1);
			fin >> newNode->diceSides;
			fin.ignore(1);
			fin >> newNode->maxDamage_magical;
			fin.ignore(1);
			fin >> newNode->weight;
			fin.ignore(1);
			fin >> newNode->hands;
			getline(fin,junk,'\n');
			newNode->next=NULL;
			cout << "!: " << newNode->name << " " << newNode->diceTimes << " " << newNode->diceSides << " " << newNode->maxDamage_magical << " " << newNode->weight<<  " " << newNode->hands << endl;
			if (first==NULL)
				first=newNode;
			else
			{
				current=first;
				if (current->next!=NULL)
				{
					while(current->next!=NULL)
						current=current->next;
					current->next=newNode;
				}
				else
				current->next=newNode;
				
			}
			count++;
		
		}
	}
}
