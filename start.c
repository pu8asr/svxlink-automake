/* Autor: Airam - PU8ASR/PX8C1730/PP8004SWL */
/* Conferência Amazônica de Radioamadorismo e Rádio do Cidadão */
/* http://conferenciaamazonica.wordpress.com */
/* airamcosta@gmail.com */
/* Contribuições são bem-vindas! */

#include<stdio.h>
#include<stdlib.h>

/* Início dos protótipos */
void limpa_tela();
int fileExists(char *cpfileName);
int decision2Options(); // Variável que recebe a decisão do usuário em relação aos backup dos arquivos
/* Fim dos protótipos */

/* Início dos códigos de tela */
/* Limpa a tela */
void limpa_tela()
{
    system("clear");
}

/* Início do código que verifica a existência de arquivos necessários nas configurações */
int fileExists(char *cpfileName)
{
    FILE *file = fopen(cpfileName, "r");
    if (!file)
        return 0; /* não existe */
    return 1; /* existe */
}
/* Fim do código que verifica a existência de arquivos necessários nas configurações */

/* Início do código onde o usuário terá que fazer escolhas */
int decision2Options()
{
    int Op; //Variável que receberá a escolha do usuário

    fflush(stdin); //Limpa o buffer do teclado para evitar erros
    printf("   Digite 1 para Sim ou 0 para Não: ");
    scanf("%d", &Op); //Aguarda a escolha do usuário
    getchar(); //Realiza uma pausa para que dê tempo para o usuário inserir a opção

    return Op;
}
/* Fim do código onde o usuário terá que fazer escolhas */

/* Incício do corpo principal da aplicação */
int main(void)
{
    int Opt; //Variável que recebe o comando do usuário (Menu)
    do
    {
        limpa_tela();
		
        printf("                       1 - Português (Brasil)\n");
        printf("                       2 - English (Coming Soon)\n");
        printf("                       3 - Español (Pronto)\n");
        printf("                       0 - Sair|Exit|Dejar\n\n\n");

        printf("   Opção|Option|Opcion: ");

        scanf("%d", &Opt);

		fflush(stdin); //Limpa o bufer de teclado evitando erros na coleta dos próximos comandos

        if (Opt == 1)
        {
			system("cd /home/pi/Downloads && wget https://github.com/pu8asr/svxlink-automake/raw/master/svxlink-install-pt_BR.c && wget https://github.com/pu8asr/svxlink-automake/raw/master/optimization-partitions.py && wget https://github.com/pu8asr/svxlink-automake/raw/master/optimization-usb.py && wget https://github.com/pu8asr/svxlink-automake/raw/master/configuration-assistent.py && gcc -g -o setup svxlink-install-pt_BR.c && ./setup && ./setup");
        }

        if (Opt == 2)
        {
			printf("\n\n                                 Invalid Option!\n");
        }

        else if (Opt == 3)
        {
			printf("\n\n                                 Opción Inválida!\n");
        }

        else if (Opt == 0)
        {
           // creditos();
		   system("sudo rm -r *");
        }

        else if (Opt > 3)
        {
            printf("\n\n                                 Opção Inválida! | Invalid Option! | Opción Inválida!\n");
        }

    } while (Opt != 0);

    return 0;
}
/* Fim do corpo principal da aplicação */
