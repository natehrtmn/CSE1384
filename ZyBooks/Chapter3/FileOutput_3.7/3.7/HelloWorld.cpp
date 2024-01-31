
#include <iostream>
#include <fstream>

int main()
{
	std::ofstream outFS;	//declare varibale

	outFS.open("data.txt");	//attempt to open file

	//Checks to see if the file had an issue opening
	if (!outFS.is_open()) {
		std::cout << "Error opening the file";
		return 1;
	}

	outFS << "What is the deal with airline food!" << std::endl;	//write to file

	outFS.close();	//closes file

	return 0;

}
