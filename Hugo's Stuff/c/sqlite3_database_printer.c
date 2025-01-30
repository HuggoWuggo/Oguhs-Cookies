#include <stdio.h>
#include <sqlite3.h>
#include <string.h>

int main() {
    sqlite3 *db;
    sqlite3_stmt *stmt;

    const char *sql = "SELECT * FROM people";
    int rc;

    rc = sqlite3_open("bmgs.db", &db);
    if (rc) {
        printf("Can't open database: %s\n", sqlite3_errmsg(db));
        return 0;
    }

    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        printf("Failed to fetch data: %s\n", sqlite3_errmsg(db));
        return 0;
    }

    // Get the number of columns
    int column_count = sqlite3_column_count(stmt);

    // Array to store the max width for each column
    int max_width[column_count];
    for (int i = 0; i < column_count; i++) {
        max_width[i] = 0;
    }
    
    int row_count = 0;
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        row_count++;
    }

    // First pass: determine the maximum width for each column
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        for (int i = 0; i < column_count; i++) {
            const char *column_text = (const char*)sqlite3_column_text(stmt, i);
            int column_len = column_text ? strlen(column_text) : 4;  // "NULL" is 4 characters long
            if (column_len > max_width[i]) {
                max_width[i] = column_len;
            }
        }
    }

    // Reset the statement for another pass
    sqlite3_reset(stmt);
   
    printf(" | ");
    for (int i = 0; i < column_count; i++) {
        const char *column_text = (const char*)sqlite3_column_name(stmt, i);
        int column_len = column_text ? strlen(column_text) : 4;
        if (column_len > max_width[i]) {
            max_width[i] = column_len;
        }
        printf("%-*s", max_width[i], column_text);
        printf(" | ");
    }

    printf("\n");
    printf(" |");

    for (int i = 0; i < column_count; i++) {
        for (int y = 0; y < max_width[i] + 2; y++) {
            printf("-");
        }
        printf("|");
    }
    printf("\n");

    sqlite3_reset(stmt);

    // Second pass: print data with padding to match the max width
    printf(" | ");
    
    int current_row = 0;

    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        current_row++;
        for (int i = 0; i < column_count; i++) {
            const char *column_text = (const char*)sqlite3_column_text(stmt, i);
            if (!column_text) {
                column_text = "NULL";
            }
            printf("%-*s", max_width[i], column_text);  // Print with left-justified padding
            printf(" | ");
        }
        printf("\n");

        if (row_count != current_row)
            printf(" | ");
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return 0;
}

