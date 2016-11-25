#include <stdio.h>
#include <stdlib.h>

void createProject()
{
	char *folderName = (char*) malloc(256*sizeof(char));

	printf(
		"You are going to create a new LaTeX project\n"
		"Enter a name for the project: ");
	scanf("%s", folderName);

	createFolder(folderName);

	free(folderName);
}

void createFolder(char* folderName)
{
	char *commandBuffer = (char*) malloc(262*sizeof(char));
	
	sprintf(commandBuffer, "mkdir %s", folderName);
	system(commandBuffer);

	free(commandBuffer);
}

void createFile()
{
	printf("%s", "Bonjoir\n");
}