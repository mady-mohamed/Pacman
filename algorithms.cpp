#include <iostream>
#include <random>
#include <cstring>
using namespace std;

extern "C" __declspec(dllexport) int heuristic(int x1, int y1, int x2, int y2, const char* ghost){
    int distance = abs(x1-x2) + abs(y1 - y2);

    if (strcmp(ghost, "RED") == 0){
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<> dis(1.0, 1.25);
        return distance * dis(gen);
    }
    else if (strcmp(ghost, "CYAN") == 0){
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<> dis(1.25, 1.5);
        return distance * dis(gen);
    }
    else if (strcmp(ghost, "PINK") == 0){
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<> dis(1.5, 1.75);
        return distance * dis(gen);
    }
    else if (strcmp(ghost, "ORANGE") == 0){
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<> dis(1.75, 2.0);
        return distance * dis(gen);
    }
    else {
        return static_cast<float>(distance);
    }
}