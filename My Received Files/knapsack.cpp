#include<iostream>
using namespace std;

class A
{
	private:
		char data[4];
};

class B
{
	private:
		char data[20];
};

class Knapsack
{
	private:
		int sizeCur;		//Used for Knapsack type 1
		int sizeMax;
		int weightCur;		//USed for Knapsack type 2
		int weightMax;
		string typeArr[7];
		int sizeArr[7];
		int count;
	public:
		Knapsack();
		template<class T>
		void pass(T); 
		void display();
};

Knapsack::Knapsack()
{
	sizeCur = 0;
	sizeMax = 0;
	weightCur = 0;
	weightMax = 0;
	count = 0;
}

template<class T>
void Knapsack::pass(T object)
{
	cout << sizeof(object) << " K" << endl;
	bool valid = false;
	for (int x=0;x<count;x++)
	{
		if (typeArr[x] == typeid(object).name())
		{
			valid = true;
			sizeArr[x]++;
		}
	}
	if (!valid)
	{
		typeArr[count] = typeid(object).name();
		sizeArr[count]++;
		count++;
	}
}

int main()
{
		A a;
		B b;
		Knapsack k;
		k.pass(a);
		k.pass(b);
		
		return 0;
}
	