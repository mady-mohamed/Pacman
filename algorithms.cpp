#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <algorithm>
#include <random>
#include <cstring>
using namespace std;

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2>& pair) const {
        return std::hash<T1>()(pair.first) ^ std::hash<T2>()(pair.second);
    }
};

void heapify(vector<int>& arr, int size, int rootIndex) {
    int largestIndex = rootIndex;          // Initialize largest as root
    int leftChildIndex = 2 * rootIndex + 1;        // left = 2*rootIndex + 1
    int rightChildIndex = 2 * rootIndex + 2;        // right = 2*rootIndex + 2

    // If left child is larger than root
    if (leftChildIndex < size && arr[leftChildIndex] > arr[largestIndex])
        largestIndex = leftChildIndex;

    // If right child is larger than largest so far
    if (rightChildIndex < size && arr[rightChildIndex] > arr[largestIndex])
        largestIndex = rightChildIndex;

    // If largest is not root
    if (largestIndex != rootIndex) {
        swap(arr[rootIndex], arr[largestIndex]);

        // Recursively heapify the affected sub-tree
        heapify(arr, size, largestIndex);
    }
}

// Function to build a Max-Heap from the given vector
void buildHeap(std::vector<int>& arr) {
    int size = arr.size();       // Get the size of the vector
    int startIndex = (size / 2) - 1; // Index of last non-leaf node

    // Perform reverse level order traversal
    // from last non-leaf node and heapify
    // each node
    for (int i = startIndex; i >= 0; i--) {
        heapify(arr, size, i);
    }
}

extern "C" {
    __declspec(dllexport) int** astar(int xStart, int yStart, int xGoal, int yGoal, const char *ghost, int** maze, int maze_height, int maze_width);
}

float heuristic(int xStart, int yStart, int xGoal, int yGoal, const char *ghost) {
    int distance = abs(xGoal - xStart) + abs(yGoal - yStart);
    if (strcmp(ghost, "RED") == 0) {
        return distance * 1.5f;
    }
    else if (strcmp(ghost, "ORANGE") == 0) {
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<> dis(1.75, 2.0);
        return distance * dis(gen);
    }
    else {
        return static_cast<float>(distance);
    }
}

__declspec(dllexport) int** astar(int xStart, int yStart, int xGoal, int yGoal, const char *ghost, int** maze, int maze_height, int maze_width) {
    map<pair<int, int>, pair<int, int>> came_from;
    map<pair<int, int>, int> cost_score = { {make_pair(xStart, yStart), 0} };
    map<pair<int, int>, int> astar_score = { {make_pair(xStart, yStart), static_cast<int>(heuristic(xStart, yStart, xGoal, yGoal, ghost))} };
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> open_list;
    open_list.push({static_cast<int>(heuristic(xStart, yStart, xGoal, yGoal, ghost)), {xStart, yStart}});

    while (!open_list.empty()) {
        auto current = open_list.top().second;
        open_list.pop();
        int currentX = current.first;
        int currentY = current.second;

        if (currentX == xGoal && currentY == yGoal) {
            vector<pair<int, int>> path_vector;
            while (came_from.find(current) != came_from.end()) {
                path_vector.push_back(current);
                current = came_from[current];
            }
            path_vector.push_back(make_pair(xStart, yStart));
            reverse(path_vector.begin(), path_vector.end());

            int path_length = path_vector.size();
            int** path = new int*[path_length + 1];  // +1 for the end marker
            for (int i = 0; i < path_length; ++i) {
                path[i] = new int[2];
                path[i][0] = path_vector[i].first;
                path[i][1] = path_vector[i].second;
            }
            path[path_length] = new int[2];
            path[path_length][0] = -1;
            path[path_length][1] = -1;

            return path;
        }

        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (const auto& direction : directions) {
            auto neighbor = make_pair(currentX + direction.first, currentY + direction.second);
            if (0 <= neighbor.first && neighbor.first < maze_height && neighbor.second < maze_width && (maze[neighbor.first][neighbor.second] == 0 || maze[neighbor.first][neighbor.second] == 1 || maze[neighbor.first][neighbor.second] == 17)) {
                int cost = cost_score[current] + 1;
                if (cost_score.find(neighbor) == cost_score.end() || cost < cost_score[neighbor]) {
                    came_from[neighbor] = current;
                    cost_score[neighbor] = cost;
                    astar_score[neighbor] = cost + static_cast<int>(heuristic(neighbor.first, neighbor.second, xGoal, yGoal, ghost));
                    open_list.push({astar_score[neighbor], neighbor});
                }
            }
        }
    }
    return nullptr;
}

int main() {
    return 0;
}