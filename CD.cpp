#include <vector>
#include <set>
#include <iostream>
using namespace std;

int main()
{
	int jacknum;
	cin >> jacknum;
	int jillnum;
	cin >> jillnum;
	int catnum;
	while (jacknum != 0 && jillnum != 0)
	{
		set<int> cds;
		for (int i = 0; i < jacknum; i++)
		{
			cin >> catnum;
			cds.insert(catnum);
		}

		int both = 0;

		for (int i = 0; i < jillnum; i++)
		{
			cin >> catnum;
			if (cds.count(catnum) == 1)
			{
				both++;
			}
		}
		cout << both << endl;
		cin >> jacknum;
		cin >> jillnum;

	}

	return 0;
}