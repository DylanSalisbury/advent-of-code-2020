#include <iostream> 
#include <list> 
#include <map>
#include <iterator> 
#include <iostream>
using namespace std;

// Compile with something like:
//
// clang main.cc -o main -l stdc++

void print(const list<int> &l) {
  for (auto i: l) {
    cout << i << " ";
  }
  cout << endl;
}

int main(void) {
    // int first[9] = { 3, 8, 9, 1, 2, 5, 4, 6, 7 };
    int first[9] = { 2, 1, 9, 3, 4, 7, 8, 6, 5 };
    int num_first_cups = 9;
    int num_cups = 1000 * 1000;
    int num_rounds = 10 * 1000 * 1000;

    // Represent the cups as a non-circular doubly-linked list, with the "front" being the
    // next element to play.
    list<int> l;

    // Map of every int to its element in the list
    map<int, list<int>::iterator> m;

    for (int i = 0; i < num_cups; ++i) {
      if (i < num_first_cups) {
        m[first[i]] = l.insert(l.end(), first[i]);
      }
      else {
        m[i+1] = l.insert(l.end(), i+1);
      }
    }

    // print(l);
    for (int round = 0; round < num_rounds; ++round) {
      if (round % 10000 == 0) {
        cout << "round " << round << endl;
      }
      list<int>::iterator iter = next(l.begin());
      int val1 = *iter;
      int val2 = *next(iter);
      int val3 = *next(next(iter));

      int target_val = *l.begin() - 1;
      if (target_val == 0) {
        target_val = num_cups;
      }
      while (target_val == val1 || target_val == val2 || target_val == val3) {
        --target_val;
        if (target_val == 0) {
          target_val = num_cups;
        }
      }

      // cout << "target " << target_val << ", lifted " << "..." << val1 << "..." << val2 << "..." << val3 << endl;
      l.splice(next(m[target_val]), l, iter, next(next(next(iter))));
      int z = l.front();
      l.pop_front();
      m[z] = l.insert(l.end(), z);

      // print(l);
    }

    // print(l);

    cout << "Elements after 1 are: ";
    list<int>::iterator print_iter = next(m[1]);
    for (int i = 0; i < 10; ++i) {
      if (print_iter == l.end()) {
        print_iter = l.begin();
      }
      cout << *print_iter << " ";
      ++print_iter;
    }
    cout << endl;
    return 0;
}
