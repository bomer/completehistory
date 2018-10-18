#include <list>
using namespace std;

enum Direction { UP, DOWN, LEFT, RIGHT };

struct Step
{
	int x;
	int y;
	int num_adj_paths;
	Direction heading;
};

class Maze
{
	private:
		int **maze;
		list<Step> path;
		int width;
		int height;

		int Turn(Step&);

		//Add more private functions here


	public:
		Maze();
		~Maze();
		
		void Run();
		int LoadData();
		void FindPath();
		void PrintMaze();
		
};
