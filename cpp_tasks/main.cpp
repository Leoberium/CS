#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string line, word;
    size_t line_count = 0, word_count = 0;
    while ( getline(cin, line) ) {
        if ( !line.empty() ) {
            istringstream words(line);
            size_t n = 0;
            while ( words >> word ) n++;
            if (n > 0) {
                line_count++;
                word_count += n;
            }
        }
    }
    cout << line_count << ' ' << word_count << '\n';
    return 0;
}
