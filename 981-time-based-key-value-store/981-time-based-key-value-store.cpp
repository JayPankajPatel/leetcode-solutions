class TimeMap {
private:
    std::unordered_map<string, std::vector<std::pair<string, int>>> time_ds; 
public:
    
    TimeMap() {}
    
    void set(std::string key, std::string value, int timestamp) {
        time_ds[key].push_back({value, timestamp}); 
        
    }
    
    string get(string key, int timestamp) {
        int l = 0; 
        int r = time_ds[key].size()-1;
        int boundary_index = -1; 
        
        while(l <= r) {
            
            int mid = (r+l)/2; 
            int prevtimestamp = time_ds[key][mid].second; 
            if(prevtimestamp <= timestamp) {
                boundary_index = mid; 
                l = mid + 1; 
            }
            
            else
                r = mid - 1;
        }
        
        if(boundary_index == -1)
            return ""; 
        else
            return time_ds[key][boundary_index].first; 
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */