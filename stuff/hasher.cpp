#include <iostream>
#include <unordered_map>
#include <fstream>
#include <string>
#include <cstring>

class values {
    public:
        std::string hashval;
        std::string fileWriteName;
        size_t hash;
        bool isFile = false;
} vals;

void argchecker(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++)
    {
        if (i + 1 != argc)
        {
            if (strcmp(argv[i], "--value") == 0 || strcmp(argv[i], "-v") == 0)
            {
                vals.hashval = argv[i + 1];
                std::cout << "You input was: " << vals.hashval << "\n" << std::endl;
                i++;
            }
            else if (strcmp(argv[i], "-w") == 0 || strcmp(argv[i], "--write") == 0)
            {
                vals.isFile = true;
                vals.fileWriteName = argv[i + 1];
                std::cout << "The file you are writing to is called: " <<vals.fileWriteName << "\n" << std::endl;
            }
        }
    }
}

void writeFile() {
    std::ofstream out(vals.fileWriteName + ".txt");
    out << vals.hash;
    out << "\n";
    out.close();
}

int main(int argc, char *argv[]) 
{
    if (argc != 1)
    {
        argchecker(argc, argv);
        std::hash<std::string> hasher;

        vals.hash = hasher(vals.hashval);

        std::cout << vals.hash << std::endl;

        if (vals.isFile == true)
        {
            writeFile();
        }
    }
}
