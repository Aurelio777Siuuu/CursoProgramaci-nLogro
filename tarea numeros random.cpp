tarea

#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

int main() {
    int cantidad, rangoMin, rangoMax;
    
    std::cout<<"¿Cuántos números quieres generar?:";
    std::cin>>cantidad;
    std::cout<<"ingresa el rango mínimo: ";
    std::cin>>rangoMin;
    std::cout<<"ingresa el rango máximo: ";
    std::cin>>rangoMax;
    
    std::srand(std::time(0));
    
    std::vector<int>numeros;
    for(int i=0; i<cantidad; ++i){
        int numeroAleatorio= rangoMin + std::rand()%(rangoMax - rangoMin + 1);
        
        numeros.push_back(numeroAleatorio);
    }
    
    std::cout<<"Sus números aleatorios generados son:\n";
    for(int numero : numeros) {
        std::cout<<numero<<" ";
    }
    std::cout<<std::endl;
    
    return 0;
}