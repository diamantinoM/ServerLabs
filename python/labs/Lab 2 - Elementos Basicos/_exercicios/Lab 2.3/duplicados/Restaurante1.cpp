#include <iostream>

using namespace std;

int main() {
	int opcao = -1;
	
	while (opcao != 0) {
		cout << endl << endl
		     << "MENU PRINCIPAL"        << endl
			 << "1 - Reservar mesa"     << endl
			 << "2 - Libertar mesa"     << endl
			 << "0 - Terminar programa" << endl;
		
		cout << "Escolha uma opção > ";
		cin >> opcao;
		
		if (opcao == 1)
			cout << "Opcao RESERVAR MESA escolhida" << endl;

		else if (opcao == 2)
			cout << "Opcao LIBERTAR MESA escolhida" << endl;
			
		else if (opcao == 0)
			cout << "Opcao TERMINAR PROGRAMA escolhida" << endl;
	}
	
	
	return 0;
}

