class Characteristics{
	private:
		string name;
		int Strength;
		int Intellegence;
		int Wisdom;
		int Dexterity;
		int Constitution;
		int Charisma;
	public:
		void setCharacteristics(string,int,int,int,int,int,int);
};

class Person{
	private:
		string name;
		string race;
	public:
		void setPerson(string);
};

class Helmets{
	private:
		struct Node;
		struct Node
		{
			string name;
			int maxArmour;
			int minArmour;
			int maxArmour_magical;
			int weight;
			
			Node *next;
		};
		Node *first;
	public:
		Helmets();
};

class Shields{
	private:
		struct Node;
		struct Node
		{
			string name;
			int maxArmour;
			int minArmour;
			int maxArmour_magical;
			int weight;
			
			Node *next;
		};
		Node *first;
	public:
		Shields();
};

class Armour{
	private:
		struct Node;
		struct Node
		{
			string name;
			int maxArmour;
			int minArmour;
			int maxArmour_magical;
			int weight;
			
			Node *next;
		};
		Node *first;
	public:
		Armour();
};

class Weapons{
	private:
		struct Node;
		struct Node
		{
			string name;
			int diceTimes;
			int diceSides;
			int maxDamage_magical;
			int weight;
			int hands;
			
			Node *next;
		};
		Node *first;
	public:
		Weapons();
};


class Race{
	private:
		Characteristics ch;
		Person p;
		struct Node;
		struct Node
		{
			string name;
			int Strength;
			int Intellegence;
			int Wisdom;
			int Dexterity;
			int Constitution;
			int Charisma;
			
			Node *next;
		};
		Node *first;
	public:
		Race();
		
};

