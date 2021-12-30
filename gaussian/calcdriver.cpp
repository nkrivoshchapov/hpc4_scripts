#include <mpi.h>
#include <stdio.h>
#include <list>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
#define MAXCHAR 1000
#define MYINTLEN 5
static char processor_name[MPI_MAX_PROCESSOR_NAME];

void to_string(int a, char *myint) {
    for(int i = 0; i < MYINTLEN;++i)
        myint[i] = '\0';
    sprintf(myint, "%d", a);
}

int main (int argc, char** argv) {
    MPI_Init(NULL, NULL);
    int world_size, world_rank, name_len;

    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Get_processor_name(processor_name, &name_len);
    printf("Hello world from processor %s, rank %d out of %d processors\n", processor_name, world_rank, world_size);

    if(world_rank == 0){
        ifstream file(argv[1]);
        list<string> calclist;
        string str;
        while (std::getline(file, str))
            calclist.push_back(str);
        string molname;
        int size;
        for(int i = 1; i < world_size;++i) {
            if(calclist.empty())
                break;
            molname = calclist.back();
            cout << "[MASTER] Sending for calculation " << molname << endl;
            size = molname.size();
            MPI_Send(&size, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
            MPI_Send(molname.c_str(), size, MPI_CHAR, i, 0, MPI_COMM_WORLD);
            calclist.pop_back();
        }
        int alive_threads = world_size;
        bool done;
        while(alive_threads > 1) {
            MPI_Status status;
            cout << "[MASTER] Waiting for done signal" << endl;
            MPI_Recv(&done, 1, MPI_C_BOOL, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);
            cout << "[MASTER] Got a signal" << endl;
            if(calclist.empty()){
                size = 0;
                --alive_threads;
                cout << "[MASTER] To go: " << alive_threads << endl;
                MPI_Send(&size, 1, MPI_INT, status.MPI_SOURCE, 0, MPI_COMM_WORLD);
            } else {
                molname = calclist.back();
                size = molname.size();
                MPI_Send(&size, 1, MPI_INT, status.MPI_SOURCE, 0, MPI_COMM_WORLD);
                MPI_Send(molname.c_str(), size, MPI_CHAR, status.MPI_SOURCE, 0, MPI_COMM_WORLD);
                calclist.pop_back();
            }
        }
        cout << "[MASTER] Terminating" << endl;
    } else {
        char *str = new char[MAXCHAR];
        char myint[MYINTLEN];
        int size, ret;
        bool done;
        to_string(world_rank, myint);
        while(true) {
            for(int i = 0; i < MAXCHAR; ++i)
                str[i]='\0';
            cout << "[WORKER] Waiting for signal" << endl;
            MPI_Recv(&size, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            cout << "[WORKER] Received a signal" << endl;
            if(size == 0)
                break;
            MPI_Recv(str, size, MPI_CHAR, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            string name, namel;
            for(int i =0;i<MAXCHAR;++i)
                if(str[i] != '\0')
                    name+=str[i];
                else
                    break;
            
            cout << "[WORKER] Process of rank " << world_rank << " is running " << name << endl;
            name = string(argv[2]) + " " + name + " " + myint;
            strcpy(str, name.c_str());
            cout << "[WORKER] " << str;
            system(str);
            cout << "[WORKER] Rung has finished" << endl;
            done = true;
            MPI_Send(&done, 1, MPI_C_BOOL, 0, 0, MPI_COMM_WORLD);
        }
        cout << "[WORKER] Terminating" << endl;
        delete str;
    }
    MPI_Finalize();
}

