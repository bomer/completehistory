#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
#include "funcs.h"

struct CdInfo
{
	int IdNum;
	char CdTitle[256];
	char RecArtist[256];
	int Mins;
	int Secs;
	float Price;
	int Stock;
	char Genre[15];
};

CdInfo CDS[200];

void YourLoadDB() // Loads the info from the data file. 
{
	int count = 0;

	for(int i = 0; i < 200; i++) //This will help determine which slots in the array are empty later on
	{
		CDS[i].IdNum = -1;
	}
	ifstream instream;
	instream.open("CDSample.txt"); // Opens the data file
	if (instream.fail())
	{
		cerr << "Could not open CDSample.txt" << endl;
	}
	else
	{
		while(!instream.eof()) // Adds all the info from the file
		{	
			instream >> CDS[count].IdNum;
			instream.ignore();
			instream.getline (CDS[count].CdTitle, 256);
			instream.getline (CDS[count].RecArtist, 256);
			instream >> CDS[count].Mins;
			instream >> CDS[count].Secs;
			instream.ignore();
			instream >> CDS[count].Price;
			instream.ignore();
			instream >> CDS[count].Stock;
			instream.ignore();
			instream.getline (CDS[count].Genre, 15);
			count++;
		}
		count--;
		instream.close();	// closes file
		cout << endl << "CDWeb has loaded " << count << " different records." << endl;
	}
}

void PrintMenu() // Opens up the menu
{
	cout << endl << "CDWeb Inventory\nCommands Available:\n";
	cout << "  A - Add new CD record.\n";
	cout << "  C - Change the stock level.\n";
	cout << "  D - Display a selected title.\n";
	cout << "  L - List by genre or artist.\n";
	cout << "  M - Print this menu.\n";
	cout << "  S - Store the in-memory DB onto file.\n";
	cout << "  V - Summarise the value of the current inventory.\n";
	cout << "  R - Remove a CD record.\n";
	cout << "  Q - Terminate the program." << endl;
}

void YourAddCD() // The adding of a new cd
{
	int count = 3; //TURN INTO GLOBAL SOMEHOW
	char command;

	cout << "You have selected to add a new CD" << endl << "Please input the ID Number of the record." << endl;
	cin >> CDS[count].IdNum;	
	cout << "Please input the record title." << endl; //ERROR Skips it 
	cin.getline (CDS[count].CdTitle, 256, '\n');
	cout << "Please input the recording artist." << endl; 
	cin.getline (CDS[count].RecArtist, 256, '\n');
	cout << "Please input the lenght of the record, input the minutes and THEN the seconds." << endl; 
	cin >> CDS[count].Mins;
	cin >> CDS[count].Secs;
	cout << "Please input the price of the record." << endl << "$"; 
	cin >> CDS[count].Price;
	cout << "Please input the amount of current stock for this record." << endl; 
	cin >> CDS[count].Stock;
	cout << "Please select the appropriate genre of the record." << endl; 
	cout << "P - Pop" << endl;
	cout << "D - Dance" << endl;
	cout << "R - R&B" << endl;
	cout << "S - Soul" << endl;
	cout << "O - Sound Track" << endl;
	cout << "K - Spoken" << endl;
	cout << "E - Easy Listening" << endl;
	cout << "C - Rock" << endl;
	cout << "T - Trance" << endl;
	cout << "A - Dance/Electric" << endl;
	cout << "H - Hip Hop/Rap" << endl;
	cin >> command;
	switch (command) // Inputing the genre from a specific list. 
		{
			case 'P':
				strcpy (CDS[count].Genre, "Pop");
				break;
			case 'D':
				strcpy (CDS[count].Genre, "Dance");
				break;
			case 'R':
				strcpy (CDS[count].Genre, "R&B");
				break;
			case 'S':
				strcpy (CDS[count].Genre, "Soul");
				break;
			case 'O':
				strcpy (CDS[count].Genre, "Sound Track");
				break;
			case 'K':
				strcpy (CDS[count].Genre, "Spoken");
				break;
			case 'E':
				strcpy (CDS[count].Genre, "Easy Listening");
				break;
			case 'C':
				strcpy (CDS[count].Genre, "Rock");
				break;
			case 'T':
				strcpy (CDS[count].Genre, "Trance");
				break;
			case 'A':
				strcpy (CDS[count].Genre, "Dance/Electric");
				break;
			case 'H':
				strcpy (CDS[count].Genre, "Hip Hop/Rap");
				break;
			default :
				cerr << "Illegal command entered." << endl;
		}
}

void YourDisplayCD() //Goes through entire array until the record is found, if its not found it returns an error message.  
{
	int finder = 0, IdNum;
	
	cout << "Please input the ID Number of the record you wish to find." << endl;
	cin >> IdNum;
	while(IdNum != CDS[finder].IdNum && finder < 200)
	{
		finder++;
	}
	if (IdNum == CDS[finder].IdNum) //  Display the record if found 
	{
		cout << "The record has been found." << endl;
		cout << "The record title is " << CDS[finder].CdTitle << "." << endl; 
		cout << "The artist is " << CDS[finder].RecArtist << "." << endl; 
		cout << "The length of the record is "<< CDS[finder].Mins << "Mins " << CDS[finder].Secs << "Secs." << endl; 
		cout << "The price of the record is $" << CDS[finder].Price << "." << endl; 
		cout << "There are " << CDS[finder].Stock << " copies currently in stock." << endl; 
		cout << "The genre is " << CDS[finder].Genre << "." << endl; 
	}
	else
	{
		cout << "Sorry but record " << IdNum << " is currently not in the database." << endl; // ERROR wont print IdNum
	}
}

void YourModifyStockLevel() //Goes through the cds to find the one the user is searching for and then allows them to modify the stock.
{
	int finder = 0, IdNum, modifier;

	cout << "Please input the ID Number of the record of which you would like to modify the current stock." << endl;
	cin >> IdNum;
	while(IdNum != CDS[finder].IdNum && finder < 200)
	{
		finder++;
	}
	if (IdNum == CDS[finder].IdNum) 
	{
		cout << "The record has been found." << endl;
		cout << "The record title is " << CDS[finder].CdTitle << " and there are " << CDS[finder].Stock << " copies currently in stock." << endl; 
		cout << "Please enter the amount you would like to decrease or increase the stock by. (Please type a '-' before the number if you wish to decrease the stock)" << endl;
		cin >> modifier;
		CDS[finder].Stock += modifier;
		if (CDS[finder].Stock < 0) // Will check if the stock falls below 0.
		{
			cout << "CDWeb has detected that the current stock is less than 0, CDWeb will adjust the current stock to 0." << endl;
			CDS[finder].Stock = 0;
		}
		else
		{
			cout << "There are now "<< CDS[finder].Stock << " copies in stock." << endl;
		}
	}
	else
	{
		cout << "Sorry but record " << IdNum << " is currently not in the database." << endl; // ERROR wont print IdNum
	}
}

void YourList()
{
	char command, RecArtist[256], Genre[15];
	bool found = false;

	cout << "Please enter your search criteria." << endl << "A - Artist" << endl << "G - Genre" << endl;
	cin >> command;
	switch(command)
	{
		case 'A': //Search by Artist
			cout << "Please enter in the name of the recording artist." << endl;
			cin.getline (RecArtist, 256, '\n'); // ERROR 
			for(int i = 0; i < 200; i++)
			{
				if(strcmp (CDS[i].RecArtist, RecArtist) == 0 && CDS[i].IdNum != -1) // use string compare 
				{
					cout << "The record has been found." << endl;
					cout << "The record title is " << CDS[i].CdTitle << "." << endl; 
					cout << "The length of the record is "<< CDS[i].Mins << "Mins " << CDS[i].Secs << "Secs." << endl; 
					cout << "The price of the record is $" << CDS[i].Price << "." << endl; 
					cout << "There are " << CDS[i].Stock << " copies currently in stock." << endl; 
					cout << "The genre is " << CDS[i].Genre << "." << endl << endl; 
					cout << "The records ID Number is " << CDS[i].IdNum << "." << endl << endl; 
					found = true;
				}
			}
			if(!found)
			{
				cout << "CDWeb could not find a match in its database." << endl;
			}
			break;
		case 'G': // Search by genre
			cout << "Please select the appropriate genre of the record." << endl; 
			cout << "P - Pop" << endl;
			cout << "D - Dance" << endl;
			cout << "R - R&B" << endl;
			cout << "S - Soul" << endl;
			cout << "O - Sound Track" << endl;
			cout << "K - Spoken" << endl;
			cout << "E - Easy Listening" << endl;
			cout << "C - Rock" << endl;
			cout << "T - Trance" << endl;
			cout << "A - Dance/Electric" << endl;
			cout << "H - Hip Hop/Rap" << endl;
			cin >> command;
			switch (command) // Inputing the genre from a specific list. 
			{
				case 'P':
					strcpy (Genre, "Pop");
					cout << Genre << endl;
					break;
				case 'D':
					strcpy (Genre, "Dance");
					break;
				case 'R':
					strcpy (Genre, "R&B");
					break;
				case 'S':
					strcpy (Genre, "Soul");
					break;
				case 'O':
					strcpy (Genre, "Sound Track");
					break;
				case 'K':
					strcpy (Genre, "Spoken");
					break;
				case 'E':
					strcpy (Genre, "Easy Listening");
					break;
				case 'C':
					strcpy (Genre, "Rock");
					break;
				case 'T':
					strcpy (Genre, "Trance");
					break;
				case 'A':
					strcpy (Genre, "Dance/Electric");
					break;
				case 'H':
					strcpy (Genre, "Hip Hop/Rap");
					break;
				default :
					cerr << "Illegal command entered." << endl;
			}
			for(int i = 0; i < 200; i++)
			{
				if(strcmp (CDS[i].Genre, Genre) == 0 && CDS[i].IdNum != -1)  // use string compare 
				{
					cout << "The record has been found." << endl;
					cout << "The record title is " << CDS[i].CdTitle << "." << endl; 
					cout << "The artist is " << CDS[i].RecArtist << "." << endl; 
					cout << "The length of the record is "<< CDS[i].Mins << "Mins " << CDS[i].Secs << "Secs." << endl; 
					cout << "The price of the record is $" << CDS[i].Price << "." << endl; 
					cout << "There are " << CDS[i].Stock << " copies currently in stock." << endl; 
					cout << "The records ID Number is " << CDS[i].IdNum << "." << endl << endl; 
					found = true;
				}
			}
			if(!found)
			{
				cout << "There are currently no " << Genre << " titles in the database." << endl;
			}
			break;				
	}
}			
		
