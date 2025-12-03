#include <stdio.h>


/*esercizio media*/


int main(){

    int a;
    int b;
    float media;

    printf("inserisci il primo numero: ");
    scanf("%d", &a);

    printf("inserisci un numero: ");
    scanf("%d", &b);

    media = (a + b ) / 2.0;

    printf("la media è: %.2f\n", media);

    return 0;
    

}
