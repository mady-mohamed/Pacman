#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <algorithm>
#include <random>
#include <cstring>
using namespace std;

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

    /**
     A* pathfinding algorithm.
     
     This function implements the A* pathfinding algorithm to find the shortest path
     from a start position to a goal position in a given maze. The maze is represented
     as a 2D array where [0, 1, 17] indicates a walkable cell indicates
     a special type of cell.
     
     @param xStart The x-coordinate of the start position.
     @param yStart The y-coordinate of the start position.
     @param xGoal The x-coordinate of the goal position.
     @param yGoal The y-coordinate of the goal position.
     @param ghost A string representing the type of ghost (e.g., "RED", "ORANGE").
     @param maze A 2D array representing the maze.
     @param maze_height The height of the maze.
     @param maze_width The width of the maze.
     @return A 2D array representing the path from the start to the goal. Each element
             is a pair of coordinates (x, y). The array is terminated with a pair (-1, -1).
     */
    map<pair<int, int>, pair<int, int>> came_from; 
    // map to keep track of path
    // key: coordinate of the current node (where the ghost is currently located).
    // value: coordinate of the parent node (where the ghost was located before moving to the current node).
    map<pair<int, int>, int> cost_score = { {make_pair(xStart, yStart), 0} };
    // Map: keep track of cost based on previous moves
    // Key: coordinates of previous node
    // Value: cumalative cost of previous moves to reach current node from start
    map<pair<int, int>, int> astar_score = { {make_pair(xStart, yStart), static_cast<int>(heuristic(xStart, yStart, xGoal, yGoal, ghost))} };
    // Map: document A* scores of start to goal
    // Key: coordinates of start node
    // Value: A* function of current node
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> open_list;
    /* 

    Priority queue to manage the open list of nodes to be evaluated Each element is a pair where the first element is the A* score and the second element is the coordinates of the node. The queue is ordered by the A* score from lowest to highest
    pair<int, pair<int, int>>:
        - first element is A* score
        - second element is coordinates of node
    vector<pair<int, pair<int, int>>>:
        - store elements of priority queue
    greater<pair<int, pair<int, int>>>:
        - This is the comparison function used to order the elements in the priority queue.
        - greater means that the priority queue will be a min-heap, where the element with the smallest A* score will be at the top.

    */
    open_list.push({static_cast<int>(heuristic(xStart, yStart, xGoal, yGoal, ghost)), {xStart, yStart}});
    // push node and heuristic function in priority queue

    while (!open_list.empty()) {
        auto current = open_list.top().second;
        open_list.pop();
        int currentX = current.first;
        int currentY = current.second;
        // Get the node with the lowest A* score from the priority queue
        // Remove the node from the priority queue
        // Extract the coordinates of the current node


        if (currentX == xGoal && currentY == yGoal) { // check if goal has been reached
            vector<pair<int, int>> path_vector; // vector to keep track of score
            while (came_from.find(current) != came_from.end()) { // loop to reconstruct path
                path_vector.push_back(current);  // push current coordinate to path
                current = came_from[current]; // change current to be parent node
                // follows chain of nodes stored in came_from map
            }
            path_vector.push_back(make_pair(xStart, yStart));
            reverse(path_vector.begin(), path_vector.end()); // reverse path to be from start to goal

            int path_length = path_vector.size();
            int** path = new int*[path_length + 1]; // set path length
            for (int i = 0; i < path_length; ++i) { // loop through path
                path[i] = new int[2]; // allocates memory for an array of 2 ints (x, y)
                path[i][0] = path_vector[i].first; // x coord
                path[i][1] = path_vector[i].second;// y coord
            }

            //represent end of path as (-1, -1)
            path[path_length] = new int[2];
            path[path_length][0] = -1;
            path[path_length][1] = -1;

            return path;
        }

        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // Possible movement directions (right, down, left, up)
        for (const auto& direction : directions) {
            auto neighbor = make_pair(currentX + direction.first, currentY + direction.second); // Calculate the neighbor's coordinates
            // Check if the neighbor is within the maze bounds and is a walkable cell (0, 1, or 17)
            if (0 <= neighbor.first && neighbor.first < maze_height && 0 <= neighbor.second && neighbor.second < maze_width && 
                (maze[neighbor.first][neighbor.second] == 0 || maze[neighbor.first][neighbor.second] == 1 || maze[neighbor.first][neighbor.second] == 17))  {
                int cost = cost_score[current] + 1; // Calculate the cost to reach the neighbor
                // If the neighbor is not in the cost_score map or the new cost is lower than the existing cost
                if (cost_score.find(neighbor) == cost_score.end() || cost < cost_score[neighbor]) {
                    came_from[neighbor] = current; // Update the parent of the neighbor to the current node
                    cost_score[neighbor] = cost; // Update the cost to reach the neighbor
                    astar_score[neighbor] = cost + static_cast<int>(heuristic(neighbor.first, neighbor.second, xGoal, yGoal, ghost)); // Calculate the A* score for the neighbor
                    open_list.push({astar_score[neighbor], neighbor}); // Add the neighbor to the priority queue with its A* score
                }
            }
        }
    }
    return nullptr;
}

int main() {
    return 0;
}