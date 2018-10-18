/**************************************************************************************
		Author: 	Blake Maddick
		Date: 		14/04/08
		Comment:	
**************************************************************************************/
#include <iostream>
using namespace std;

int main()
{
	int number, temp, div = 1, single; 

	cout << endl;
	cout << "Enter integer: " << endl;
	cin >> number;
	cout << number << " = ";
	single = number;
	while (single > 9) 
	{
		single = single / 10;
		div = div * 10;
	}
//	single = 1  --  div = 10000
	while (number > 0)
	{
		number = number % div

	}
return 0;
}


//		number = number % div;
//		cout << number << " + "; 
//		div = div * 10;


/*	while (number > 0)
	{
		current = number / div;
			if (current > 9)
				div * 10;			
	else
				cout << current << endl;

		number = number % div;
		div = 1;
 	}
*/

	/*
	bravo 	=	alpha % 	10;
	charlie =	alpha % 	100 		/ 10;
	delta 	=	alpha % 	1000 		/ 100;
	echo 	=	alpha % 	10000 		/ 1000;
	foxtrot =	alpha % 	100000 		/ 10000;
	golf 	=	alpha % 	1000000 	/ 100000;
	hotel 	=	alpha % 	10000000 	/ 1000000;
	india 	=	alpha %		100000000 	/ 10000000;
	*/

