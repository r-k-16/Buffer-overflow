#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

void copy(char str[8000]){ //Vulnerable function
  char cpy[267];
  strcpy(cpy, str); //Vulnerable section
}
void start_server(){
    char str[8000], cpy[267];
    int sfd, cfd;
 
    struct sockaddr_in sock;
 
    sfd = socket(AF_INET, SOCK_STREAM, 0);
 
    bzero(&sock, sizeof(sock));
 
    sock.sin_family = AF_INET;
    sock.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    sock.sin_port = htons(8888); //Binding port
 
    bind(sfd, (struct sockaddr *) &sock, sizeof(sock));
 
    listen(sfd, 10);
 
    cfd = accept(sfd, (struct sockaddr*) NULL, NULL);

    char response[] = "Hello from server!\n\n";
    send(cfd, response, strlen(response), 0);
 
    while(1){
        read(cfd,str,8000);
        copy(str);
        puts(str);
        write(cfd, str, strlen(str)+1);
    }
}
int main(int argc, char **argv){
    start_server();
}
