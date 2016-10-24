#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main(){

	std::ifstream f;
	f.open("s.txt");
	std::string lnum;
	
	if(f.is_open()){
		f>>lnum;
	}

	int maxProd = 0;
    int currProd;
    std::vector<int> v{0,0,0,0,0};

	for(int i=0; i<lnum.length(); i++){
        v[i%5] = lnum[i] - '0';
        
        currProd = std::accumulate(v.begin(),
                                    v.end(),
                                    1,
                                    [](int x, int y){return x*y;});
		if(currProd > maxProd){
			maxProd = currProd;
		}
	}

	printf("The max prod is %d\n", maxProd);

}

