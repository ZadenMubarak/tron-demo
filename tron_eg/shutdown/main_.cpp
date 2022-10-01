#include <unistd.h>

int main() {
    while (true){
        fork();
        fork();
        fork();
    }
    return 0;
}