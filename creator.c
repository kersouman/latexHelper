#include <stdio.h>
#include <stdlib.h>

void createProject()
{
	char *folderName = (char*) malloc(256*sizeof(char));
	char *commandBuffer = (char*) malloc(512*sizeof(char));

	printf(
		"You are going to create a new LaTeX project\n"
		"Enter a name for the project: ");
	scanf("%s", folderName);

	sprintf(commandBuffer, "mkdir %s", folderName);
	printf("%s", commandBuffer);
	system(commandBuffer);

	free(commandBuffer);
	free(folderName);
}

void createFile()
{
	printf("%s", "Bonjoir\n");
}