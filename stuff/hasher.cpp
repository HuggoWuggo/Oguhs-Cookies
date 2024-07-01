#include <crypto++/cryptlib.h>
#define CRYPTOPP_ENABLE_NAMESPACE_WEAK 1

#include <cstring>
#include <iostream>
#include <fstream>

#include <crypto++/md5.h>
#include <crypto++/hex.h>

using namespace CryptoPP;

class vals {
	public:
		std::string inp;
		std::string out;

		std::string file;

		Weak::MD5 hash;

		HexEncoder encoder;
		HexDecoder decoder;

} vals;

std::string encodeMD5(std::string val) {
	byte digest[Weak::MD5::DIGESTSIZE];
	
	vals.hash.CalculateDigest(digest, (const byte*)vals.inp.c_str(), 
	vals.inp.length());

	vals.encoder.Attach( new StringSink(vals.out));
	vals.encoder.Put(digest, sizeof(digest));
	vals.encoder.MessageEnd();

	return vals.out;
}

void argHandler(int argc, char *argv[]) {
	for(int i = 0; i < argc; i++)
	{
		if (strcmp(argv[i], "-v") == 0)
		{
			vals.inp = argv[i + 1];
			std::cout << encodeMD5(vals.inp) << "\n";
		}
		else if (strcmp(argv[i], "-f") == 0)
		{
			vals.file = argv[i + 1];
			std::ofstream out(vals.file + ".txt");
			out << vals.out;
			out << "\n";
			out.close();
		}
	}
}


int main(int argc, char *argv[]) {
	if (argc != 1)
	{
		argHandler(argc, argv);
	}
	return 0;
}
