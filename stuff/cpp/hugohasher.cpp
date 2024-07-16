#include <crypto++/cryptlib.h>
#define CRYPTOPP_ENABLE_NAMESPACE_WEAK 1

#include <cstring>
#include <iostream>
#include <fstream>
#include <sstream>

#include <crypto++/md5.h>
#include <crypto++/hex.h>

using namespace CryptoPP;

class vals {
	public:
		std::string inp;
		std::string out;

		std::string file;
		std::string encFile;

		Weak::MD5 hash;

		HexEncoder encoder;
		
		bool hasInp = false;

} vals;

std::string encodeMD5(std::string val) {
	std::string final;
	byte digest[Weak::MD5::DIGESTSIZE];
	
	vals.hash.CalculateDigest(digest, (const byte*)val.c_str(), 
	val.length());

	vals.encoder.Attach( new StringSink(final));
	vals.encoder.Put(digest, sizeof(digest));
	vals.encoder.MessageEnd();

	vals.out = final;

	return final;
}

void writeFile(std::string filename, std::string contents) {
	std::ofstream out(filename);
	out << contents;
	out << "\n";
	out.close();
}

void argHandler(int argc, char *argv[]) {
	for(int i = 0; i < argc; i++)
	{
		if (strcmp(argv[i], "-h") == 0) {
			std::cout << 
			"WELCOME TO HUGO HASHER!\n\n" 
			"-h = shows this message\n"
			"-v = specfies what string you want to hash (use "" for multiple words)\n"
			"-o = specifies what file you want to write to\n"
			"-f = specfies if you want to hash the contents of a file (but not write it)\n\n"
			"SPECIFY what hashing algorithm you want to use\n"
			"-eMD5 = use md5 algorithm"
			<< std::endl;
		}

		else if (strcmp(argv[i], "-v") == 0)
		{
			vals.inp = argv[i + 1];
			vals.hasInp = true;
		}
		else if (strcmp(argv[i], "-o") == 0)
		{
			vals.file = argv[i + 1];
			writeFile(vals.file, vals.out);
		}

		else if (strcmp(argv[i], "-f") == 0)
		{
			vals.file = argv[i + 1];
			std::ifstream outfile(vals.file);
			std::string contents;
			std::string line;

			if (!outfile.is_open()) { 
        		std::cerr << "Error opening the file!" << std::endl; 
    		}

			while(!outfile.eof()) 
			{
					
				// extracting line from file.txt 
				getline(outfile, line); 
				if (line != "")
				{
					line = encodeMD5(line);
				}
				contents += line;
				contents += "\n";
			}
			vals.out = contents;
			std::cout << contents << std::endl;
		}

		else if (strcmp(argv[i], "-eMD5") == 0 && vals.hasInp == true)
		{
			std::cout << encodeMD5(vals.inp) << std::endl;
		}
		
	}
}

int main(int argc, char *argv[]) {
	if (argc != 1)
	{
		argHandler(argc, argv);
	}
	else {
		std::cout << "Please enter some args! (-h for more)" << std::endl;
	}
	return 0;
}
