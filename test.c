// COMMAND TO COMPILE PROGRAM  
// gcc file_name.c -o name_of_the_output_file
// In this case gcc test.c -o test 
// then simply run test.exe in the respective directory

#define _GNU_SOURCE
#include <stdio.h> 
#include<conio.h> 
#include<stdlib.h> 
#include<string.h> 
#include<stdbool.h> 
#define book_names_location "C:/Code/Files/book_names.txt"

struct Membership {
    char *username;
    char *password; 
    char *date_of_birth;
    char *email_id;
    char *phone_number;
}; 
// struct Membership* custom_struct = malloc(sizeof (struct Membership) + 100 * sizeof(int));

struct Book {
    char *name;
    char *author;
    char *genre; 
    char *type;
};


void display_lend_book_options();
void display_lend_book_options(){
    printf(" ************************************************************ WELCOME **************************************************** \n"); 
    printf("1) Lend a Book \n");
    printf("2) Return a Book \n");
    printf("3) Add a Book \n");
    printf("4) Previous Menu \n");
    printf("5) Exit \n");
    printf("Enter your choice \n");

}

void display_book_names(); 
void display_book_names(){
    FILE *file_pointer; 
    char** book_names;  
    ssize_t length; 
    char *line = NULL; 
    size_t len = 0;

    file_pointer = fopen(book_names_location, "r");
    while((length = getline(&line, &len, file_pointer)) != -1) {
        book_names = " " ;// WIP 
    }

    if(line)
        free(line);

    fclose(file_pointer);
}


void handle_user_page_options(int choice);
void handle_user_page_options(int choice){
    struct Book book;
    int user_input; 
    switch(choice){
        case 1: 
            system("cls");
            printf("These are the available books for lending \n");
            display_book_names();
            break ;

        case 2: 
            // Return a Book 
            break ;

        case 3: 
            book.name = (char *)malloc( 100 * sizeof(char) ); 
            book.author = (char *)malloc( 100 * sizeof(char) ); 
            book.genre = (char *)malloc( 100 * sizeof(char) ); 
            book.type = (char *)malloc( 100 * sizeof(char) ); 
            add_a_book(&book);
            break ; 

        case 4: 
            render_main_menu();
            scanf("%d", &user_input);
            handle_main_menu_cases(user_input);
            break; 

        case 5: 
            exit(0);
            break; 
            
        default: 
            printf("Invalid Input \n"); 
            int choice; 
            display_lend_book_options();
            scanf("%d", &choice);
            handle_user_page_options(choice);
    }
}


void render_main_menu() {
    system("cls");
    printf("Enter your choice !! \n");
    printf("1) New Membership  \n"); 
    printf("2) Existing Membership \n");
    printf("3) Exit \n ");
}

// Might be used for future references
// void swap(int *x, int *y);
// void swap(int *x, int *y){
//     int temp;
//     temp = *x; 
//     *x = *y; 
//     *y = temp; 
// }
 
void input_user_details(struct Membership *object); 
void input_user_details(struct Membership *object) {
        printf("Enter Username \n"); 
        scanf("%s", (*object).username);
        printf("Enter Password \n ");
        scanf("%s", (*object).password);
        printf("Enter Date Of Birth \n"); 
        scanf("%s", (*object).date_of_birth);
        printf("Enter Email Id \n"); 
        scanf("%s", (*object).email_id);
        printf("Enter Phone Number \n");
        scanf("%s", (*object).phone_number);
}

void add_a_book(struct Book *book);
void add_a_book(struct Book *book){
    FILE *file_pointer; 
    char content[1000];
    char file_location[100] = "C:/Code/Files/Books/";
    system("cls");
    printf("Name of Book \n"); 
    scanf("%s", (*book).name); 
    printf("Name of Author \n"); 
    scanf("%s", (*book).author); 
    printf("Genre of Book \n "); 
    scanf("%s", (*book).genre);
    printf("Type of the Book \n"); 
    scanf("%s", (*book).type);

    strcat(file_location, book->name); 
    strcat(file_location, ".txt"); 
    
    file_pointer = fopen(file_location, "a+"); 

    if(file_pointer == NULL) {
        printf("Unable to Save Book Details.  Please try again !!"); 
        exit(EXIT_FAILURE);
    }

    fputs(book->name, file_pointer);
    fputs("\n", file_pointer);
    fputs(book->author, file_pointer);
    fputs("\n", file_pointer);
    fputs(book->genre, file_pointer);
    fputs("\n", file_pointer);
    fputs(book->type, file_pointer);
    fputs("\n", file_pointer);
    fclose(file_pointer);
    
    // Below lines of code are written to make a file which would contain names of all books and add the name of the book to that file.
    FILE *pointer; 
    pointer = fopen(book_names_location, "a+"); 
    fputs(book->name, pointer); 
    fputs("\n", pointer);
    fclose(pointer);


    printf("The Book has been successfully added to the database \n"); 
    free(book);
    int choice; 
    display_lend_book_options();
    scanf("%d", &choice);
    handle_user_page_options(choice);
}


void save_details_in_a_file(struct Membership *object); 
void save_details_in_a_file(struct Membership *object) {
    FILE * file_pointer; 
    char content[1000]; 
    char file_location[100] = "C:/Code/Files/";
    strcat(file_location, object->username);
    strcat(file_location, ".txt");
    file_pointer = fopen(file_location, "a+");

    if (file_pointer == NULL)
    {
        printf("Unable to create and save to file \n "); 
        exit(EXIT_FAILURE);
    }

    strcat(content, object->username);
    strcat(content, " "); 
    strcat(content, object->password);
    strcat(content, " ");
    strcat(content, object->date_of_birth);
    strcat(content, " ");
    strcat(content, object->email_id); 
    strcat(content, " "); 
    strcat(content, object->phone_number);
    strcat(content, "\n");

    fputs(content, file_pointer); 
    fclose(file_pointer);
    free(object);    
}

bool is_email_validated(char email[]); 
bool is_email_validated(char email[]){
    if((strstr(email, "@") != NULL ) && (strstr(email, ".com") != NULL)) {
        return true;
    }
    return false;
}

bool is_username_unique(char username[]); 
bool is_username_unique(char username[]){
    FILE *file_pointer; 
    char file_location[100] = "C:/Code/Files/";
    strcat(file_location, username);
    strcat(file_location, ".txt");
    if(file_pointer = fopen(file_location, "r")) {
        fclose(file_pointer);
        return false;
    }
    return true;
}

bool check_if_valid_credentials(char username[], char password[]);
bool check_if_valid_credentials(char username[], char password[]){
    FILE *file_pointer; 
    char file_location[100] = "C:/Code/Files/";
    int count = 0 ;
    char word[20];

    strcat(file_location, username);
    strcat(file_location, ".txt");
    
    if(file_pointer = fopen(file_location, "r")) {
        while(fscanf(file_pointer, "%99s", word) != EOF){
            if(++count == 2) {
                if (strcmp(word, password) == 0) {
                    return true;
                } else{
                    return false;
                }
            }
        }
    fclose(file_pointer);
    }
    else{
        printf("Sorry, user not found :( ");
        return false;
    }
}

void handle_main_menu_cases(int variable); 
void handle_main_menu_cases(int var) {
    switch(var) {
        struct Membership membership; 
        case 1: 
            membership.username = (char *)malloc( 50 * sizeof(char) ); 
            membership.password = (char *)malloc( 50 * sizeof(char) ); 
            membership.date_of_birth = (char *)malloc( 50 * sizeof(char) ); 
            membership.email_id = (char *)malloc( 50 * sizeof(char) ); 
            membership.phone_number = (char *)malloc( 50 * sizeof(char) ); 
            system("cls"); // Clears The Screen (takes arguments as commands which can be used in command  prompt)
            input_user_details(&membership);
            if (is_email_validated(membership.email_id) && is_username_unique(membership.username)) {
                save_details_in_a_file(&membership);
                printf("Your membership has been created. \n Have a nice day :D ");
                printf("%s", membership.username);
            }
            else {
                int choice;
                printf("There seems to be something wrong with the values you have provided. Please have a look");
                render_main_menu();
                scanf("%d", &choice);
                handle_main_menu_cases(choice);        
            }
            break;

        case 2: 
            system("cls");
            char *username; 
            char *password;
            username = (char*)malloc(strlen(username)*sizeof(char));
            password = (char*)malloc(strlen(password)*sizeof(char));
            printf("Enter username -> \n");
            scanf("%s", username);
            printf("Enter password -> \n ");
            scanf("%s", password);
            if (check_if_valid_credentials(username, password)) {
                free(username);
                free(password);
                int choice; 
                system("cls");
                display_lend_book_options();
                scanf("%d", &choice); 
                handle_user_page_options(choice);
                exit(0);
            } else {
                int choice;
                free(username);
                free(password);
                printf("Sorry, user not found. Please try again");
                render_main_menu();
                scanf("%d", &choice);
                handle_main_menu_cases(choice);        
                
            }
            
            break;

        case 3: 
            exit(0);
            break;

        default: 
            break; 
    }
}

int main() 
{   
    int choice = 0; 
    render_main_menu();
    scanf("%d", &choice);
    handle_main_menu_cases(choice);
    
    return  0;
}
