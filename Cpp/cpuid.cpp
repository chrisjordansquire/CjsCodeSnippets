#include <stdint.h>
#include <iostream>
#include <bitset>

// Fun w/ inline assembler.

using namespace std;

class CpuId{
    uint32_t regs[4];

    public:
        void load(unsigned i){
            asm volatile("cpuid" : "=a" (regs[0]), "=b" (regs[1]), "=c" (regs[2]), "=d" (regs[3])
       : "a" (i), "c" (0));
        }

        const uint32_t &EAX() const{return regs[0];}
        const uint32_t &EBX() const{return regs[1];}
        const uint32_t &ECX() const{return regs[2];}
        const uint32_t &EDX() const{return regs[3];}
};


int main(){
    
    int n=1;
    char cn = (char) n;
    if( cn == 1 ){
        cout << "Little Endian\n\n";
    }
    else{
        cout << "Big Endian\n\n";
    }

    CpuId cpuId;
    cpuId.load(0);
    
    cout << hex << cpuId.EAX() << "\n";
    string vendor;
    vendor += string((const char *)&cpuId.EBX(), 4);
    vendor += string((const char *)&cpuId.EDX(), 4);
    vendor += string((const char *)&cpuId.ECX(), 4);

    cout << "CPU vendor = " << vendor << endl;
    cout << "\n";

    cpuId.load(1);
    
    cout << bitset<32>(1) << "\n";
    cout << bitset<32>(cpuId.EAX()) << "\n";
    cout << bitset<32>(cpuId.EBX()) << "\n";
    cout << bitset<32>(cpuId.ECX()) << "\n";
    cout << bitset<32>(cpuId.EDX()) << "\n";
    cout << "\n";

    cpuId.load(2);
     
    cout << hex << cpuId.EAX() << "\n";
    cout << hex << cpuId.EBX() << "\n";
    cout << hex << cpuId.ECX() << "\n";
    cout << hex << cpuId.EDX() << "\n";
    cout << "\n";

    cpuId.load(7);
     
    cout << hex << cpuId.EBX() << "\n";

    return 0;
}
