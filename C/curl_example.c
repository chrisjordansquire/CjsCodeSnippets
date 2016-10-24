#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>
#include <string.h>


void requestWebpage(char* url);

int main() {

    requestWebpage((char *) "http://www.google.com");
    return 0;
}

struct Response{
    char *buffer;
    size_t size;
};

size_t write_data(void *curl_data, size_t numberOfElements, size_t sizePerElement, void *user_buffer){
    struct Response* response = (struct Response*) user_buffer;
    size_t totalBytes = numberOfElements * sizePerElement;
    printf("the curl data\n");
    printf("%s\n\n", (char *) curl_data);
    response->buffer = (char *) realloc(response->buffer, response->size + totalBytes + 1);
    if(response->buffer == NULL){
        printf("not enough memory returned\n");
        return 0;
    }
    memcpy(&(response->buffer[response->size]), curl_data, totalBytes);
    response->size += totalBytes;
    response->buffer[response->size] = 0;
}

void requestWebpage(char* url){

    struct Response response;
    response.buffer = (char *) malloc(1);
    response.size = 0;

    CURL *curl;
    curl_global_init(CURL_GLOBAL_DEFAULT);

    curl = curl_easy_init();
    if(!curl){
        return;
    }

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *) &response);
    CURLcode returnCode;
    returnCode = curl_easy_perform(curl);
    curl_easy_cleanup(curl);

    printf("the written response data\n");
    printf("%s\n", response.buffer);
    curl_global_cleanup();
    free(response.buffer);
}
