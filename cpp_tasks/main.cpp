#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int word_counter() {
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

char alphabet[36] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z'};

void to_k(long n, long k) {
    if (n / k != 0) {
        to_k(n / k, k);
    }
    cout << alphabet[n % k];
}

int main() {
    long k, t, n = 0;
    cin >> k >> t;
    string s;
    cin >> s;
    for (char c : s) {
        n = n * k + long(c <= '9' ? c - '0' : c - 55);
    }
    to_k(n, t);
    cout << endl;
    return 0;
}