#include "creator.h"
#include <stdio.h>
#include <string.h>

void dispatcher(const char* arg[])
{
	if (strcmp(arg[1], "new") == 0)
	{
		if (strcmp(arg[2], "project") == 0)
		{
			createProject();
		}
		else if (strcmp(arg[2], "file") == 0)
		{
			createFile();
		}
	}
}

int main(int argc, const char* argv[])
{
	dispatcher(argv);

	return 0;
}