#include <iostream>
#include <string>

using namespace std;

int main()
{
    string input;
    getline(cin,input);
    int lc = 0, uc = 0, ws = 0, sym = 0;
    for (int i = 0; i < input.length(); i++)
    {
        int code = input[i];
        if (code >= 'A' && code <= 'Z')
            uc++;
        else if (code >= 'a' && code <= 'z')
            lc++;
        else if (code == '_')
            ws++;
        else
            sym++;
    }
    cout << double(ws)/input.length() << "\n" << double(lc)/input.length() << "\n" << double(uc)/input.length() << "\n" << double(sym)/input.length() << endl;
}