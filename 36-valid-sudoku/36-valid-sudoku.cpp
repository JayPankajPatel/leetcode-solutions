class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        using namespace std;
        unordered_set<string>seen; 
        
        
       for(int i = 0; i < 9; i++){
           
           for(int j = 0; j < 9; j++){
               string cur(1,board[i][j]);
               if(cur == ".")
                   continue; 
               if(seen.find(cur + " found in row " + to_string(i)) != seen.end() || 
                  seen.find(cur + " found in column " + to_string(j)) != seen.end() ||
                  seen.find(cur + " found in square " + to_string((i/3) * 3 + j/3))!= seen.end()
                 )
                   return false; 
               
               seen.insert(cur + " found in row " + to_string(i));
               seen.insert(cur + " found in column " + to_string(j));
               seen.insert(cur + " found in square " + to_string((i/3) * 3 + j/3));
           }
       }
        
        
        return true;
    }
};