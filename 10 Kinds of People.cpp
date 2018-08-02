#include <vector>
#include <iostream>
#include <queue>
#include <stdio.h>

using namespace std;

class Graph
{
public:
	Graph(long num_rows, long num_cols);
	void readGraph();
	void printMatrix();
	void colorGraph();
	void colorAdjNodes(long row, long col, long color);
	vector<pair<long,long>> adjNode(long row, long col);
	vector<vector<long>> m;
	vector<vector<long>> cm;
	long m_num_rows;
	long m_num_cols;
};

Graph::Graph(long num_rows, long num_cols) : m(num_rows,vector<long>(num_cols,-1))
	, cm(num_rows,vector<long>(num_cols,-1))
	, m_num_rows(num_rows)
	, m_num_cols(num_cols)
{
}

void Graph::readGraph()
{
	char val;
	getchar();
	for (long i = 0; i < m_num_rows; i++)
	{
		for (long j = 0; j < m_num_cols; j++)
		{
			val = getchar();
			if (val == '0')
				m[i][j] = 0;
			else
				m[i][j] = 1;
		}
		getchar();
	}
	colorGraph();
}

void Graph::colorGraph()
{
	long color = 2;
	for (long i = 0; i < m_num_rows; i++)
	{
		for (long j = 0; j < m_num_cols; j++)
		{
			if (cm[i][j] == -1)
			{
				colorAdjNodes(i,j,color);
				color++;
			}

		}
	}
}

void Graph::colorAdjNodes(long row, long col, long color)
{
	queue<pair<long,long>> q;
	cm[row][col] = color;
	q.push(pair<long,long>(row,col));
	while (!q.empty())
	{
		auto curr = q.front();
		q.pop();
		auto adjlist = adjNode(curr.first,curr.second);
		for (auto & adjp : adjlist)
		{
			if (cm[adjp.first][adjp.second] == -1)
			{
				cm[adjp.first][adjp.second] = color;
				q.push(adjp);	
			}
		}
	}
}

vector<pair<long,long>> Graph::adjNode(long row, long col)
{
	vector<pair<long,long>> adjNodes;
	long bin = m[row][col];
	if (row != 0 && m[row-1][col] == bin)
	{
		adjNodes.emplace_back(pair<long,long>(row-1,col));
	}
	if (row != m_num_rows-1 && m[row+1][col] == bin)
	{
		adjNodes.emplace_back(pair<long,long>(row+1,col));
	}
	if (col != 0 && m[row][col-1] == bin)
	{
		adjNodes.emplace_back(pair<long,long>(row,col-1));
	}
	if (col != m_num_cols-1 && m[row][col+1] == bin)
	{
		adjNodes.emplace_back(pair<long,long>(row,col+1));
	}
	return adjNodes;

}


void Graph::printMatrix()
{
	cout << "\nGraph" << endl;
	for (long i = 0; i < m_num_rows; i++)
	{
		for (long j = 0; j < m_num_cols; j++)
		{
			cout << m[i][j];
		}
		cout << endl;
	}

	cout << "\nColor graph" << endl;
	for (long i = 0; i < m_num_rows; i++)
	{
		for (long j = 0; j < m_num_cols; j++)
		{
			cout << cm[i][j];
		}
		cout << endl;
	}
}

int main()
{

	long num_rows;
	cin >> num_rows;
	long num_cols;
	cin >> num_cols;

	Graph g(num_rows, num_cols);
	g.readGraph();
	//g.printMatrix();
	long nc,r1,c1,r2,c2;
	cin >> nc;
	for (long i = 0; i < nc; i++)
	{
		cin >> r1;
		cin >> c1;
		cin >> r2;
		cin >> c2;
		if (g.cm[r1-1][c1-1] != g.cm[r2-1][c2-1])
		{
			cout << "neither" << endl;
		}
		else if (g.m[r1-1][c1-1] == 0)
		{
			cout << "binary" << endl;
		}
		else
		{
			cout << "decimal" << endl;
		}
	}

	return 0;
}