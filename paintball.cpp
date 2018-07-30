#include <vector>
#include <iostream>
#include <array>
#include <stack>

using namespace std;

void printGraph(vector<vector<int>> & graph);
void findMaxFlow(vector<vector<int>> & graph);
bool getPathToSink(vector<vector<int>> & graph);

void printGraph(vector<vector<int>> & graph)
{
	for (int i = 0 ; i < graph.size(); i++)
	{
		cout << "Node " << i << ": ";
		for (int j = 0; j < graph[i].size(); j++)
		{
			cout << graph[i][j] << " ";
		}
		cout << "\n" << endl;
	}
}

void findMaxFlow(vector<vector<int>> & graph)
{

	int shooters = graph.size()/2;

	vector<vector<int>> rg(graph.size(),vector<int>(graph.size()));
	for (int i = 0; i < graph.size(); i++)
	{
		for (int j = 0; j < graph[i].size(); j++)
		{
			rg[i][graph[i][j]] = 1;
		}
	}

	while(getPathToSink(rg))
	{}
	
	vector<int> kills;
	for (int i = 1; i < shooters; i++)
	{
		bool set = false;
		for (int j = 0; j < graph[i].size(); j++)
		{
			if (rg[i][graph[i][j]] == 0)
			{
				kills.emplace_back(graph[i][j]-shooters+1);
				set = true;
			}
		}
		if (set == false)
		{
			cout << "Impossible" << endl;
			return;
		}
	}

	for (auto i : kills)
	{
		cout << i << endl;
	}
}

bool getPathToSink(vector<vector<int>> & rg)
{
	vector<int> visited(rg.size(),-1);
	stack<int> q;
	int sink = rg.size()-1;

	visited[0] = 0;
	q.push(0);

	while (!q.empty())
	{		
		if(visited[sink] != -1)
			break;

		int curr = q.top();
		q.pop();
		for (int i = 0; i < rg[curr].size(); i++)
		{
			if (rg[curr][i] == 1 && visited[i] == -1)
			{
				q.push(i);
				visited[i] = curr;
			}
		}
	}

	if (visited[sink] == -1)
	{
		return false;
	}

	int curr = sink;
	while(curr != 0)
	{
		rg[curr][visited[curr]]++;
		rg[visited[curr]][curr]--;
		curr = visited[curr];
	}
	return true;
}


int main()
{
	//get the size of the graph
	int num_players;
	cin >> num_players;
	vector<vector<int>> graph((num_players*2)+2,vector<int>());

	//read in the lines
	int num_lines;
	cin >> num_lines;

	int playera;
	int playerb;

	for (int i = 0; i < num_lines; i++)
	{
		cin >> playera;
		cin >> playerb;
		graph[playera].emplace_back(num_players+playerb);
		graph[playerb].emplace_back(num_players+playera);
	}

	for (int i = 1; i < num_players+1; i++)
	{
		graph[0].emplace_back(i);
		graph[i+num_players].emplace_back(num_players*2+1);
	}

	//printGraph(graph);
	findMaxFlow(graph);
	return 0;
}
