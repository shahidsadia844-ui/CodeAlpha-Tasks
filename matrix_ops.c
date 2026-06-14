#include <stdio.h>

#define SIZE 3 // Hum 3x3 matrices ke liye code bana rahe hain

// Functions ki declaration
void inputMatrix(int matrix[SIZE][SIZE]);
void printMatrix(int matrix[SIZE][SIZE]);
void addMatrices(int mat1[SIZE][SIZE], int mat2[SIZE][SIZE], int result[SIZE][SIZE]);
void multiplyMatrices(int mat1[SIZE][SIZE], int mat2[SIZE][SIZE], int result[SIZE][SIZE]);
void transposeMatrix(int matrix[SIZE][SIZE], int result[SIZE][SIZE]);

int main() {
    int matA[SIZE][SIZE], matB[SIZE][SIZE];
    int sum[SIZE][SIZE], product[SIZE][SIZE], transpose[SIZE][SIZE];

    printf("--- Matrix A ke elements input karein (3x3) ---\n");
    inputMatrix(matA);

    printf("\n--- Matrix B ke elements input karein (3x3) ---\n");
    inputMatrix(matB);

    // 1. Addition
    addMatrices(matA, matB, sum);
    printf("\n[1] Matrix Addition (A + B):\n");
    printMatrix(sum);

    // 2. Multiplication
    multiplyMatrices(matA, matB, product);
    printf("\n[2] Matrix Multiplication (A * B):\n");
    printMatrix(product);

    // 3. Transpose (Matrix A ka transpose)
    transposeMatrix(matA, transpose);
    printf("\n[3] Matrix A ka Transpose:\n");
    printMatrix(transpose);

    return 0;
}

// User se matrix ke elements input lene ka function
void inputMatrix(int matrix[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("Element [%d][%d]: ", i, j);
            scanf("%d", &matrix[i][j]);
        }
    }
}

// Matrix ko screen par saaf suthra print karne ka function
void printMatrix(int matrix[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

// Do matrices ko plus karne ka function
void addMatrices(int mat1[SIZE][SIZE], int mat2[SIZE][SIZE], int result[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            result[i][j] = mat1[i][j] + mat2[i][j];
        }
    }
}

// Do matrices ko multiply karne ka function
void multiplyMatrices(int mat1[SIZE][SIZE], int mat2[SIZE][SIZE], int result[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            result[i][j] = 0;
            for (int k = 0; k < SIZE; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

// Matrix ka Transpose nikalne ka function
void transposeMatrix(int matrix[SIZE][SIZE], int result[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            result[j][i] = matrix[i][j]; // Rows aur columns ko swap kar diya
        }
    }
}
