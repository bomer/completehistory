
#include"Maze.h"
#include<iterator>


Maze::Maze()
{
	width = 0;
	height = 0;
}

int Maze::LoadData()
{
	char fname[50];
	cout << "Please enter the filename for your maze: " << endl;
	cin >> fname;
	
	ifstream fin;
	fin.open(fname);
	if (!fin.good())
	{
		cerr << "Bad filename" << endl;
		exit(0);
	}
	
	fin >> width;
	fin >> height;
	cout << width << " " << height << endl;
	
	maze = new int*[height];
	for (int x=0;x<height;x++)
		maze[x] = new int[width];
	char buffer[50];
	fin.getline(buffer,50,'\n');
	for (int x=0;x<height;x++)
	{
		fin.getline(buffer,50,'\n');
		for (int y=0;y<width;y++)
		{
			maze[x][y] = static_cast<int>(buffer[y]-'0');
		}
	}
	
}

int Maze::Turn(Step &step)
{
	path.push_back(step);
	list<Step>::iterator pi;
	pi = path.end();
	pi--;
	
	cout << "HERE: " << cur.x << " " << cur.y << " " << cur.heading << " " << cur.num_adj_paths << endl;
	Direction heading = cur.heading;
	bool RIGHT = false;
	bool LEFT = false;
	cout << pi->heading << " " << cur.heading << "LKJ: " << endl;
	if (pi->heading == cur.heading)
	{
		
		cout << "rightkk: " << cur.heading << cur.x << " " << cur.y << " "<< endl;
		if (cur.heading == 0 && cur.x!=width-1)
		{
			if (maze[cur.y][cur.x+1] == 0)
			{
				cur.x++;
				cur.heading = Direction(3);
				RIGHT = true;
			}
		}
		else if(cur.heading == 1 && cur.x!=0)
		{
			if (maze[cur.y][cur.x-1] == 0)
			{
				cur.x--;
				cur.heading = Direction(2);
				RIGHT= true;
			}
		}
		else if(cur.heading == 2 && cur.y!=0)
		{
			if (maze[cur.y-1][cur.x] == 0)
			{
				cur.y--;
				cur.heading = Direction(0);
				RIGHT = true;
			}
		}
		else if(cur.heading == 3 && cur.x!=height-1)
		{
			if (maze[cur.y+1][cur.x] == 0)
			{
				cur.y++;
				cur.heading = Direction(1);
				RIGHT = true;
			}
		}
		cout << "JJ: " << cur.x << " " << cur.y << " " << cur.heading << " "  << RIGHT << endl;
		if (!RIGHT)
		{
			cur.heading = heading;
			cout << "RRRRIIIIGGGGHHHHTTTTT" << endl;
			if (cur.heading == 0 && cur.x!=0)
			{
				cur.heading = Direction(2);
				//cout << "@" << endl;
				if (maze[cur.y][cur.x-1] == 0)
				{
					cur.x--;
					LEFT = true;
					//cout << "@" << endl;
				}
			}
			else if (cur.heading == 2 && cur.y!=0)
			{
				cur.heading = Direction(1);
				if (maze[cur.y+1][cur.x] == 0)
				{
					cur.y++;
					LEFT = true;
				}
			}
			else if (cur.heading == 1 && cur.x!=width-1)
			{
				cur.heading = Direction(3);
				//cout << "#" << endl;
				if (maze[cur.y][cur.x+1] == 0)
				{
					//cout << "#" << endl;
					cur.x++;
					LEFT = true;
				}
			}
			else if (cur.heading == 3 && cur.y!=height-1)
			{
				cur.heading = Direction(0);
				//cout << "1" << endl;
				if (maze[cur.y-1][cur.x] == 0)
				{
					//cout << "2" << endl;
					cur.y--;
					LEFT = true;
				}
			}
						
		}
		cout << "JJqq: " << cur.x << " " << cur.y << " " << cur.heading << endl;
	}
	else
	{
		if (cur.heading == 0 && cur.x!=0)
		{
			cur.heading = Direction(2);
			if (maze[cur.y][cur.x-1] == 0)
			{
				//cur.x--;
				LEFT = true;
			}
		}
		else if (cur.heading == 2 && cur.y!=0)
		{
			cur.heading = Direction(1);
			if (maze[cur.y-1][cur.x] == 0)
			{
				//cur.y--;
				LEFT = true;
			}
		}
		else if (cur.heading == 1 && cur.x!=width-1)
		{
			cur.heading = Direction(3);
			if (maze[cur.y][cur.x+1] == 0)
			{
				//cur.x++;
				LEFT = true;
			}
		}
		else if (cur.heading == 2 && cur.y!=height-1)
		{
			cur.heading = Direction(0);
			if (maze[cur.y+1][cur.x] == 0)
			{
				//cur.y++;
				LEFT = true;
			}
		}
		if (pi->heading == cur.heading)
		{
			if (LEFT)
			{
				if (cur.heading == 0)
					cur.y++;
				else if (cur.heading == 1)
					cur.y--;
				else if (cur.heading == 3)
					cur.x++;
				else if (cur.heading == 2)
					cur.x--;
			}
		}
	}		

	if (LEFT || RIGHT)
		return true;
	else
		return false;
}
	

void Maze::PrintMaze()
{
	for (int x=0;x<height;x++)
	{
		for (int y=0;y<width;y++)
		{
			cout << maze[x][y];
		}
		cout << endl;
	}
}

void Maze::FindPath()
{
	//----finding entrance point
	bool found = false;
	int count = 0;
	Step s;
	s.num_adj_paths = 0;
	for (int x=0;x<width;x++)//checking top wall
	{
		if (maze[0][x] == 0)
		{
			s.y = 0;
			s.x = x;
			s.heading = DOWN;
			if (maze[0][x+1] == 0)
				s.num_adj_paths++;
			if (maze[0][x-1] == 0)
				s.num_adj_paths++;
			if (maze[1][x] == 0)
				s.num_adj_paths++;
			path.push_back(s);
			found = true;
			break;
		}
	}
	if (!found)
	{
		for (int x=0;x<height;x++)
		{
			if (maze[x][0] == 0)
			{
				s.y = x;
				s.x = 0;
				s.heading = RIGHT;
				if (maze[x+1][0] == 0)
					s.num_adj_paths++;
				if (maze[x-1][0] == 0)
					s.num_adj_paths++;
				if (maze[x][1] == 0)
					s.num_adj_paths++;
				path.push_back(s);
				found = true;
				break;
			}
		}
	}
	list<Step>::iterator ip;
	for (ip=path.begin();ip!=path.end();ip++)
		cout << "Entry Point: " << ip->y << " " << ip->x << " " << ip->num_adj_paths << " " << ip->heading << endl;
		
	//------------------------finding exit point ---------------------------
	Step exit;//exit point
	found = false;
	for (int x=0;x<width;x++)//checking top wall
	{
		if (maze[height-1][x] == 0)
		{
			exit.y = height-1;
			exit.x = x;
			found = true;
			break;
		}
	}
	if (!found)
	{
		for (int x=0;x<height;x++)
		{
			if (maze[x][width-1] == 0)
			{
				exit.y = x;
				exit.x = width-1;
				found = true;
				break;
			}
		}
	}
	cout << "exit point is: " << exit.y << " " << exit.x << endl;
	//list<Step>::iterator ip;
	ip=path.begin();
	Step next;
	cur.x = ip->x;
	cur.y = ip->y;
	cur.heading = ip->heading;
	cur.num_adj_paths = ip->num_adj_paths;
	Direction heading;
	bool EXIT = false;
	bool move = false;
	while(!EXIT)
	{
		
		move = false;
		if (cur.heading == 0 && cur.y!=0)
		{
			if (maze[cur.y-1][cur.x] == 0)
			{
				cur.y--;
				move = true;
			}
		}
		else if(cur.heading == 1 && cur.y!=height-1)
		{
			if (maze[cur.y+1][cur.x] == 0)
			{
				cur.y++;
				move = true;
			}
		}
		else if(cur.heading == 2 && cur.x!=0)
		{
			if (maze[cur.y][cur.x-1] == 0)
			{
				cur.x--;
				move = true;
			}
		}
		else if(cur.heading == 3 && cur.x!=width-1)
		{
			if (maze[cur.y][cur.x+1] == 0)
			{
				cur.x++;
				move = true;
			}
		}
		//for (ip=path.begin();ip!=path.end();ip++)
			//cout << "Path: " << ip->x << " " << ip->y << " " << ip->heading << " " << ip->num_adj_paths << endl;
		//cout << "Cur: " << cur.x << " " << cur.y << " " << cur.heading << " " << cur.num_adj_paths << endl;
		bool TURN = false;
		if (!move)
		{
			cur.num_adj_paths = 0;
			if (maze[cur.y+1][cur.x] == 0 && cur.y!=height-1)
				cur.num_adj_paths++;
			if (maze[cur.y-1][cur.x] == 0 && cur.y!=0)
				cur.num_adj_paths++;
			if (maze[cur.y][cur.x+1] == 0 && cur.x!=width-1)
				cur.num_adj_paths++;
			if (maze[cur.y][cur.x-1] == 0 && cur.x!=0)
				cur.num_adj_paths++;
			//cout << "DD: " << cur.num_adj_paths << endl;
			if (cur.num_adj_paths == 1)
			{
				//cout << "Path11: " << ip->x << " " << ip->y << " " << ip->heading << " " << ip->num_adj_paths << endl;
				
				while(1)
				{
					ip = path.end();
					ip--;
					cout << "Path11: " << ip->x << " " << ip->y << " " << ip->heading << " " << ip->num_adj_paths << endl;
					if (ip->num_adj_paths > 2)
					{
						ip = path.end();
						ip--;
						cur.x = ip->x;
						cur.y = ip->y;
						cur.num_adj_paths = ip->num_adj_paths;
						cur.heading = ip->heading;
						break;
					}
					else
					{
						path.pop_back();
						cout << "POPPED: " << endl;
						//cout << "IP: " << ip->x << " " << ip->y << " " << endl;
					}
				}		
			}
			
			if (Turn(cur) == 0)
				TURN = false;
			else
				TURN = true;
			cout << "TURN: " << TURN << endl;
			while (!TURN)
			{
				while (1)
				{
					ip = path.end();
					ip--;
					if (ip->num_adj_paths > 2)
					{
						TURN = true;
						break;
					}
					else
					{
						path.pop_back();
						//ip = path.end();
						//ip--;
						//cout << "IP: " << ip->x << " " << ip->y << " " << endl;
					}
				}
			}
		}
		if (count !=0)
		{
			if (cur.x == 0 || cur.x == width-1 || cur.y== 0 || cur.y==height-1)
			{
				EXIT = true;
				cout << "EXXXIIITTT" << endl;
			}
		}
		if (!EXIT)
		{
			cur.num_adj_paths = 0;
			if (maze[cur.y+1][cur.x] == 0 && cur.y!=height-1)
				cur.num_adj_paths++;
			if (maze[cur.y-1][cur.x] == 0 && cur.y!=0)
				cur.num_adj_paths++;
			if (maze[cur.y][cur.x+1] == 0 && cur.x!=width-1)
				cur.num_adj_paths++;
			if (maze[cur.y][cur.x-1] == 0 && cur.x!=0)
				cur.num_adj_paths++;
			cout << "Cur2: " << cur.x << " " << cur.y << " " << cur.heading << " " << cur.num_adj_paths << endl;
			//maze[cur.y][cur.x] = 5;
			//PrintMaze();
			cout << "------------------------------------------------" << endl;
			path.push_back(cur); 
		}
		count++;
		//cout << "count: " << count << endl;
		char ch;
		cin >> ch;
	}

}

void Maze::Run()
{
	LoadData();
	PrintMaze();
	FindPath();
	
}
